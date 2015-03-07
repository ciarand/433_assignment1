import math

from .interface import CipherInterface

class TranspositionCipher(CipherInterface):
    """
    The TranspositionCipher class.

    In this case, the key represents the column ordering.
    """

    def set_key(self, key):
        if not isinstance(key, str):
            raise TypeError("expected string, got %r" % key)

        if not key.isdecimal():
            raise TypeError("expected an all decimal key, got %s", key)

        self.key = key

    def create_rails(self, rows, cols):
        rails = [[]] * rows

        for r in range(rows):
            rails[r] = [None] * cols

        return rails

    def dimensions(self, txt):
        cols = len(self.key)

        rows = math.ceil(len(txt) / cols)

        return (rows, cols)

    def encrypt(self, plaintext):
        txt = plaintext.strip()

        numrows, numcols = self.dimensions(txt)

        rails = self.create_rails(numrows, numcols)

        # first write out the encryption rail-by-rail
        rowi = coli = 0
        for letter in plaintext:
            rails[rowi][coli] = letter
            coli += 1
            if coli >= numcols:
                rowi += 1
                coli = 0

        # encryption reads off according to the key order
        result = ""
        for col in self.key:
            c = int(col) - 1
            for row in range(numrows):
                if rails[row][c] != None:
                    result += rails[row][c]
                else:
                    result += 'Z'

        print("rails=%r, key=%s, text=%s, result=%s" % (rails, self.key, txt, result))
        return result

    def populate_rails(self, txt):
        numrows, numcols = self.dimensions(txt)

        rails = self.create_rails(numrows, numcols)

        gen = iter(txt)

        for col in self.key:
            for r in range(numrows):
                try:
                    val = next(gen)
                    print("rails[%d][%d] = %r" % (r, int(col)-1, val))
                    rails[r][int(col) - 1] = val
                except StopIteration:
                    rails[r][int(col) - 1] = 'Z'

        return rails

    def decrypt(self, ciphertext):
        txt = ciphertext.strip()

        rails = self.populate_rails(txt)

        # decryption reads off rail-by-rail
        result = ""
        for r in rails:
            for c in r:
                print("decrypt: adding column %r from rails box %r to result %s" % (c, rails, result))
                if c != None:
                    result += c

        print("rails=%r, key=%s, text=%s, result=%s" % (rails, self.key, txt, result))
        return result


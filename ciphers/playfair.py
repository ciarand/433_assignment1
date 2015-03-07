import itertools

from .interface import CipherInterface

class PlayfairCipher(CipherInterface):
    """
    The PlayfairCipher class.

    In this case, the key represents the chosen keyword and will be converted
    into a matrix (list of 5char strings).

    This implementation relies on the Wikipedia entry for the Playfair cipher:
    http://en.wikipedia.org/wiki/Playfair_cipher
    """

    def get_digraphs(self, plaintext):
        """
        Separates out the given plaintext into a set of digraphs (ending with
        a Z if the number of characters is odd).
        """

        plaintext = plaintext.upper().strip()

        digraphs = []

        i = 0
        length = len(plaintext)

        while i < length:
            first = plaintext[i]

            i += 1
            # safely grab the second letter
            if i < length:
                second = plaintext[i]
            else:
                second = 'Z'

            # append the tuple to the result
            digraphs.append((first, second))

            i += 1

        return digraphs


    def set_key(self, key):
        if not isinstance(key, str) or not key.isalpha:
            raise TypeError

        # combine j and i to make the alphabet fit in a 5x5 box (25 chars)
        key = key.replace("J", "I").upper()

        # technically we only really need space for 25 characters as j will
        # never be used but it's easier to expand it by 1 than implement the if
        # letter > 'j' nonsense.
        chosen = [False] * 26

        k = ""
        # iterate through each character in the key, ignoring dupes
        for char in key:
            pos = self.letter_to_pos(char)

            if not chosen[pos]:
                chosen[pos] = True
                k += char

        alphaString = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphaString:
            pos = self.letter_to_pos(char)

            if not chosen[pos]:
                chosen[pos] = True
                k += char

        assert len(k) == 25, "expected length of key (%r) to be 25" % len(k)

        self.key = [k[0:5], k[5:10], k[10:15], k[15:20], k[20:]]

    def create_digraph(self, frow, fcol, srow, scol: int) -> tuple:
        """ Creates a digraph (a tuple of chars) from the given row + col
        numbers.
        """

        return (self.key[frow][fcol], self.key[srow][scol])

    def encrypt_digraph(self, dg):
        """ Takes a digraph and encrypts it, returning an encrypted digraph. """

        first, second = dg

        if first == second:
            second = 'X'

        frow, fcol = self.location_of(first)
        srow, scol = self.location_of(second)

        # If the letters appear on the same row of your table, replace them with the
        # letters to their immediate right respectively (wrapping around to the left
        # side of the row if a letter in the original pair was on the right side of the
        # row).
        if frow == srow:
            fcol, scol = (fcol + 1) % 5, (scol + 1) % 5

        # If the letters appear on the same column of your table, replace them with the
        # letters immediately below respectively (wrapping around to the top side of
        # the column if a letter in the original pair was on the bottom side of the
        # column).
        if fcol == scol:
            frow, srow = (frow - 1) % 5, (srow - 1) % 5

        # If the letters are not on the same row or column, replace them with
        # the letters on the same row respectively but at the other pair of
        # corners of the rectangle defined by the original pair. The order is
        # important – the first letter of the encrypted pair is the one that
        # lies on the same row as the first letter of the plaintext pair
        if frow != srow and fcol != scol:
            fcol, scol = scol, fcol

        return self.create_digraph(frow, fcol, srow, scol)

    def decrypt_digraph(self, dg):
        """ Takes an encrypted digraph and decrypts it, returning a plaintext
        digraph
        """

        first, second = dg

        # this rule remains the same
        if first == second:
            second = 'X'

        frow, fcol = cipher_frow, cipher_fcol = self.location_of(first)
        srow, scol = cipher_srow, cipher_scol = self.location_of(second)

        if fcol == scol:
            # shift up this time (plus)
            frow, srow = (frow + 1) % 5, (srow + 1) % 5

        if frow == srow:
            # shift left this time (minus)
            fcol, scol = abs((fcol - 1) % 5), abs((scol - 1) % 5)

        # this one's the same from a code perspective too
        if frow != srow and fcol != scol:
            fcol, scol = scol, fcol

        return self.create_digraph(frow, fcol, srow, scol)

    def location_of(self, c: str) -> tuple:
        """ Finds the location of the provided char in the current key
        (matrix). Returns the result as a tuple containing the rownum and
        column num (`(rownum, colnum)`) - both zero indexed.
        """

        c = c.upper()
        if c == 'J': c = 'I'

        row = 0
        while row < 5:
            col = self.key[row].find(c)

            if col != -1:
                return (row, col)

            row += 1

        raise ValueError("couldn't find letter %r in matrix %r" % (c, self.key))

    def digraphs_to_string(self, digraphs):
        txt = ""
        for dg in digraphs:
            a, b = dg

            txt += a + b

        return txt

    def encrypt(self, plaintext):
        # now we have a list of digraphs
        digraphs = self.get_digraphs(plaintext)

        ciphertext = []
        for dg in digraphs: ciphertext.append(self.encrypt_digraph(dg))

        txt = self.digraphs_to_string(ciphertext)

        return txt

    def decrypt(self, ciphertext):
        # now we have a list of digraphs
        digraphs = self.get_digraphs(ciphertext)

        plaintext = []
        for dg in digraphs: plaintext.append(self.decrypt_digraph(dg))

        txt = self.digraphs_to_string(plaintext)

        return txt

import math

from cipher_interface import CipherInterface

class RailFenceCipher(CipherInterface):
    """
    The RailFenceCipher class.

    In this case, the key represents the number of rows (rails) to use.
    """

    def set_key(self, key):
        self.key = int(key)

    def encrypt(self, plaintext):
        # first create a list of rails
        rails = [[] for _ in range(self.key)]

        for index, letter in enumerate(plaintext):
            rails[index % self.key].append(letter)

        return "".join("".join(row) for row in rails)

    def decrypt(self, ciphertext):
        # decrypting this one is a little more complicated. First we need to
        # figure out the lengths of the rails:
        clen = len(ciphertext)
        rlen = int(math.floor(clen / self.key))

        # but we may have some leftovers
        remd = clen % self.key

        lengths = [0] * self.key
        for i in range(self.key):
            if remd != 0:
                # if we still have some remainder we'll subtract from that pool
                # and add it to the current rail length.
                lengths[i] = rlen + 1
                remd -= 1
            else:
                # otherwise the length is just rlen
                lengths[i] = rlen

        rails = [""] * self.key

        # put it in rails order
        base = 0
        for railnum, raillen in enumerate(lengths):
            rails[railnum] = ciphertext[base:base+raillen]
            base += raillen

        # now read it diagonally
        plaintext = ""
        for index in range(len(ciphertext)):
            railnum = index % self.key
            charnum = int(index / self.key)

            plaintext += rails[railnum][charnum]

        return plaintext

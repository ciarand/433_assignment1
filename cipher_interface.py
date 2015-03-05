class CipherInterface:
    """
    The base class used by each xCipher class.
    """
    def __init__(self):
        self.key = None

    def set_key(self, key):
        self.key = key
        rValue = False

        if (key.isalpha):
            rValue = True

        return rValue

    def encrypt(self, plaintext):
        raise NotImplementedError

    def decrypt(self, ciphertext):
        raise NotImplementedError

    # A is 65, Z is 90 in ASCII codes. We were promised no punctuation.
    def letter_to_pos(self, letter):
        return ord(letter) - 65

    def pos_to_letter(self, pos):
        return chr((pos % 26) + 65)

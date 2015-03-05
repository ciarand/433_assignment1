from cipher_interface import CipherInterface

class CaesarCipher(CipherInterface):
    """
    The CaesarCipher class.

    In this case, the key represents the translation difference in number of
    letters.
    """

    def set_key(self, key):
        self.key = int(key)

    def encrypt(self, plaintext):
        ciphertext = ""

        for plain_letter in plaintext.upper():
            ciphertext += self.pos_to_letter(self.letter_to_pos(plain_letter) + self.key)

        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""

        for cipher_letter in ciphertext.upper():
            plaintext += self.pos_to_letter(self.letter_to_pos(cipher_letter) - self.key)

        return plaintext

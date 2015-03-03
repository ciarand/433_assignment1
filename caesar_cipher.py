from cipher_interface import CipherInterface

class CaesarCipher(CipherInterface):
    """
    The Caesar cipher class.

    In this case, the key represents the translation difference in number of
    letters.
    """

    def encrypt(self, plaintext):
        ciphertext = ""

        for plain_letter in plaintext.upper():
            # A is 65, Z is 90 in ASCII codes. We were promised no punctuation.
            ciphertext += self.pos_to_letter(self.letter_to_pos(plain_letter) + self.key)

        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""

        for cipher_letter in ciphertext.upper():
            plaintext += self.pos_to_letter(self.letter_to_pos(cipher_letter) - self.key)

        return plaintext

    def letter_to_pos(self, letter):
        return ord(letter) - 65

    def pos_to_letter(self, pos):
        return chr((pos % 26) + 65)

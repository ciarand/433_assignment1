from .interface import CipherInterface

class VigenreCipher(CipherInterface):
    """
    The VigenreCipher class.

    In this case, the key represents the chosen keyword.
    """

    def encrypt(self, plaintext):
        keylength = len(self.key)

        ciphertext = ""
        for index, letter in enumerate(plaintext):
            difference = self.letter_to_pos(self.key[index % keylength])

            ciphertext += self.pos_to_letter(self.letter_to_pos(letter) + difference)

        return ciphertext

    def decrypt(self, ciphertext):
        keylength = len(self.key)

        plaintext = ""
        for index, letter in enumerate(ciphertext):
            difference = self.letter_to_pos(self.key[index % keylength])

            plaintext += self.pos_to_letter(self.letter_to_pos(letter) - difference)

        return plaintext

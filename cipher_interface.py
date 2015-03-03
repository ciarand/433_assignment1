class CipherInterface:
    """
    The base class used by each xCipher class.
    """
    def __init__(self):
        self.key = None

    def set_key(self, key):
        self.key = key

    def encrypt(self, plaintext):
        raise NotImplementedError

    def decrypt(self, ciphertext):
        raise NotImplementedError

import pytest, string, random

from caesar_cipher import CaesarCipher

def generate_random(n):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(n))

def test_cipher():
    ciph = CaesarCipher()

    for i in range(1, 100):
        ciph.set_key(i % 25)
        plaintext = generate_random(i * (i % 3))

        assert plaintext == ciph.decrypt(ciph.encrypt(plaintext)), \
                "expected CaesarCipher to correctly decode plaintext %s" % plaintext


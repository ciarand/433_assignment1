import pytest, string, random

from caesar_cipher import CaesarCipher
from vigenre_cipher import VigenreCipher

def generate_random(n):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(n))

def run_cipher_tests(cipher, keyfunc):
    for i in range(1, 100):
        # create the key according to the passed in keyfunc
        cipher.set_key(keyfunc(i))

        # generate a random plaintext
        plaintext = generate_random(i * (i % 3))

        # test that the cipher encrypts and decrypts the plaintext successfully
        assert plaintext == cipher.decrypt(cipher.encrypt(plaintext)), \
                "expected %s to correctly decode plaintext %s" % (cipher, plaintext)

def test_caesar_cipher():
    run_cipher_tests(CaesarCipher(), lambda i: i % 25)

def test_vigenre_cipher():
    run_cipher_tests(VigenreCipher(), lambda i: "mylongtextkey")

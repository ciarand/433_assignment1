import pytest, string, random

from caesar_cipher import CaesarCipher
from vigenre_cipher import VigenreCipher
from railfence_cipher import RailFenceCipher

def generate_random(n):
    """
    Generates a random string, n characters long.
    """
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(n))

def run_cipher_tests(cipher, keyfunc):
    """
    Runs a series of random strings through the provided cipher. Each iteration
    the cipher's set_key function is called with the output of the keyfunc
    callback (which is passed the current iteration index).
    """
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
    run_cipher_tests(VigenreCipher(), lambda _: "mylongtextkey")

def test_railfence_cipher():
    run_cipher_tests(RailFenceCipher(), lambda i: (i % 6) + 1)

    c = RailFenceCipher()
    c.set_key(3)

    assert "cpeeryourcimtsut" == c.encrypt("computersecurity")
    assert "computersecurity" == c.decrypt("cpeeryourcimtsut")

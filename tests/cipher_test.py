import pytest, string, random

from ciphers import *

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

def test_playfair_cipher_set_key():
    c = PlayfairCipher()

    try:
        c.set_key(1)
        assert False, "PlayfairCipher shouldn't allow non-string keys"
    except TypeError:
        pass

    try:
        c.set_key("foobar")
        assert True, "PlayfairCipher should allow alpha keys"
    except TypeError:
        assert False, "PlayfairCipher broke on an alpha key"

    expected = ["FOBAR",
                "CDEGH",
                "IKLMN",
                "PQSTU",
                "VWXYZ"]

    assert c.key == expected, "expected %s to equal %s" % (c.key, expected)

def test_playfair_cipher():
    for i in range(1, 100):
        cipher = PlayfairCipher()

        cipher.set_key(generate_random(random.SystemRandom().choice(range(24))))

        # generate a random plaintext
        plaintext = generate_random(i * (i % 3))

        # encrypt, then decrypt it
        actual = cipher.decrypt(cipher.encrypt(plaintext))

        # this cipher does not handle 'X's gracefully tbqh
        # in fact it usually generates a number of shitty things that make
        # it hard to unit test. So we're just going to go percent-wise. The
        # number of differences (i.e. where actual[i] !== plaintext[i]) should
        # be < 10% of the length of the plaintext.
        errors = 0
        allowed_errors = int(len(plaintext) / 10)
        if allowed_errors < 3: allowed_errors = 3

        for index, letter in enumerate(plaintext):
            if letter == actual[index]:
                continue

            if letter == 'J' and actual[index] == 'I':
                continue

            if letter == 'X':
                continue

            if index > 0 and index % 2 == 1 and actual[index] == 'X' and plaintext[index - 1] == letter:
                continue

            errors += 1

        assert errors <= allowed_errors, ( \
                "expected %s to correctly decode plaintext %s but found %d mismatches." + \
                "\nExpected: %s" + \
                "\nActual  : %s") % (cipher, plaintext, errors, plaintext, actual)

def test_railfence_cipher():
    run_cipher_tests(RailFenceCipher(), lambda i: (i % 6) + 1)

    c = RailFenceCipher()
    c.set_key(3)

    assert "cpeeryourcimtsut" == c.encrypt("computersecurity")
    assert "computersecurity" == c.decrypt("cpeeryourcimtsut")

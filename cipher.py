#!/usr/bin/env python

# Assignment 1: CS 433
# Due: 3/6/2015
# Group: Kourun Sok, Ciaran Downey, Stratton Aguilar

'''
Usage: python3 cipher.py <CIPHER> <KEY> <ENC/DEC> <INPUT FILE> <OUTPUT FILE>

  CIPHER: The name of the cipher. Valid names are:

    – PLF: Playfair
    – RTS: Row Transposition
    – RFC: Railfence
    – VIG: Vigenre
    – CES: Caesar
    – MAC: Monoalphabetic Cipher (graduate students only)

  KEY: the encryption key to use.
  ENC/DEC: whether to encrypt or decrypt, respectively.
  INPUT FILE: the file from which to read the input.
  OUTPUT FILE: the file to which the output shall be written.
'''

import sys
from pathlib import Path

from cipher_interface import CipherInterface
from caesar_cipher import CaesarCipher
from vigenre_cipher import VigenreCipher
from railfence_cipher import RailFenceCipher

# this is where the main entry point will go

def die(msg):
    sys.stderr.write(msg + '\n')
    sys.exit(__doc__)

if __name__ == "__main__":
    if len(sys.argv) < 6:
        die("not enough arguments")

    ciph_name = sys.argv[1]
    key       = sys.argv[2]
    mode      = sys.argv[3]
    inp       = sys.argv[4]
    out       = sys.argv[5]

    # read the input data or die
    inpath = Path(inp)
    if not inpath.exists():
        die("input file '%s' doesn't exist" % inp)

    if inpath.is_dir():
        die("input file '%s' is a directory" % inp)

    indata = ""
    with inpath.open('r') as f:
        indata += f.read()

    # create a cipher or die
    if ciph_name == "PLF":
        cipher = CipherInterface()
    elif ciph_name == "RTS":
        cipher = CipherInterface()
    elif ciph_name == "RFC":
        cipher = RailFenceCipher()
    elif ciph_name == "VIG":
        cipher = VigenreCipher()
    elif ciph_name == "CES":
        cipher = CaesarCipher()
    elif ciph_name == "MAC":
        cipher = CipherInterface()
    else:
        die("Unrecognized cipher name '%s'" % ciph_name)

    # set the cipher key
    cipher.set_key(key)

    # encode or decode or die
    if mode == "ENC":
        outdata = cipher.encrypt(indata)
    elif mode == "DEC":
        outdata = cipher.decrypt(indata)
    else:
        die("Unrecognized mode '%s'" % mode)

    # write the data out (and make sure to close the file)
    with open(out, 'w') as f:
        f.write(outdata)

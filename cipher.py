#!/usr/bin/env python

'''
Assignment 1: CS 433
Due: 3/6/2015
Group: Kourun Sok, Ciaran Downey, Stratton Aguilar
'''

'''
Instruction
  CIPHER NAME: Is the name of the cipher. Valid names are:
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

./cipher <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE>
'''

import sys
import struct
import os

class cipher(CipherInterface):
    def vigenre(key, mode, input, output):
        '''
        from wiki
        C_i = E_K(M_i) = (M_i+K_i) \mod {26}
        and decryption D using the key K,

        M_i = D_K(C_i) = (C_i-K_i) \mod {26},
        '''
        # this method is really slow!!
        mode = mode.upper()
        # output for outputing either enc or dec
        save_output = ''
        # open the file
        with open(input, 'r') as f:
            plaintext = f.read().upper()
            f.close()
        key= key * len[plaintext]
        if mode =='ENC':
            for i in plaintext:
                for j in key:
                    intcitext = ord(i) + ord(j) % 26
                    save_output += chr(intcitext)
        elif mode =='DEC':
            for i in plaintext:
                for j in key:
                    intcitext = ord(i) - ord(j) % 26
                    save_output += chr(intcitext)
        # save the file to a text file
        g = open(output, 'w')
        g.write(save_output)
        g.close

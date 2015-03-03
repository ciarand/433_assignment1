'''
Assignment 1 : CS  433
Due : 3/6/2015
Group : Kourun Sok, Ciaran Downey, Stratton Aguilar
'''


'''
Instruction 
• CIPHER NAME: Is the name of the cipher. Valid names are:
– PLF: Playfair
– RTS: Row Transposition
– RFC: Railfence
– VIG: Vigenre
– CES: Caesar
– MAC: Monoalphabetic Cipher (graduate students only)
• KEY: the encryption key to use.
1• ENC/DEC: whether to encrypt or decrypt, respectively.
• INPUT FILE: the file from which to read the input.
• OUTPUT FILE: the file to which the output shall be written.
./cipher <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE>

'''
#!/usr/bin/env python

import sys
import struct
import os
     

class CipherInterface:
    '''
    define all alphabet and for encrp + k , decry - k
    have to deal with text wrap, basic cesar, only encrp/dec alphabet no special character
    '''
    def caesar(key,mode,input,output):
        mode = mode.upper()
        #output for outputing either enc or dec
        save_output = ''
        #openthe file
        with open(input,'r') as f:
            plaintext = f.read().upper()
            f.close()
       
        if mode =='ENC':
            for i in plaintext:
                    intcitext = ord(i) + key % 26
                    save_output += chr(intcitext)

        elif mode =='DEC':
           for i in plaintext:
                    intcitext = ord(i) - key % 26
                    save_output += chr(intcitext)
        #save the file to a text file
        g = open(output,'w')
        g.write(save_output)
        g.close
    
    def Vigenre(key,mode,input,output):
        '''
        from wiki
        C_i = E_K(M_i) = (M_i+K_i) \mod {26}
        and decryption D using the key K,

        M_i = D_K(C_i) = (C_i-K_i) \mod {26},
        '''
        #this method is really slow!!
        mode = mode.upper()
        #output for outputing either enc or dec
        save_output = ''
        #openthe file
        with open(input,'r') as f:
            plaintext = f.read().upper()
            f.close()
        key= key * len[plaintext]
        #start encryting loop through all character in the plaintext search if it is in the alphabet then +- with the key
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
        #save the file to a text file
        g = open(output,'w')
        g.write(save_output)
        g.close
        
            
            
        


                
       
        
        
        
        
        

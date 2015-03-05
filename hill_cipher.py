#just writing the logic out ,need to test

import numpy as np
from numpy import matrix
from numpy import linalg


def hillCipher(key,mode,input,output):
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mode = mode.upper()
    #output for outputing either enc or dec
    save_output = ''
    #openthe file
    with open(input,'r') as f:
        input = f.read().upper()
        f.close()
        #start encryting loop through all character in the plaintext search if it is in the alphabet then +- with the key
    #put key into a matraix .. using a key of 3X3 = 0=9
    for j in key[0::3]:
        tempkey = np.matrix[key]
    if mode =='ENC':
        #start encryting
        while len(input) % 3 != 0:
            #add random string to the plain text until the %3 !=3 
            gennum = random.randint(0, 25)
            input = input +  alphabet.find(gennum)
        for i in plaintext[0::3]:
            j = 0
            tempplaintext = orc(input[i:i+3])
            temparray = np.matrix[tempplaintext]
            #start the matrix multiplicity
            cipher_text1[j] = chr((tempkey * temparray) %26)
            j++
    elif mode =='DEC':
        #start decrypting
        #inverse of key matraix
        inverse = numpy.linalg.inv(tempkey)
        for i in input[0::3]:
            j = 0
            tempciphertext = orc(plaintext[i:i+3])
            temparray = np.matrix[tempciphertext]
            #start the matrix multiplicity
            plain_text1[j] = chr((inverse * temparray) %26)
            j++
     #save the file to a text file
    g = open(output,'w')
    g.write(save_output)
    g.close
        
            

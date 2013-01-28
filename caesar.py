#!/usr/bin/python
# caesar alghoritm ,the basic solution for cryptography
# hrouhi.kh@gmail.com


stdalph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
crypalph = []
shift = -3
def caesar():
  for x in range(0,26):
		crypalph.append(stdalph[(x+shift)%26])
	message = raw_input('message:')
	cryptmessage =''
	for x in message:
		if stdalph.count(x):
			cryptmessage += crypalph[stdalph.index(x.lower())]
		else:
			cryptmessage += x
	print cryptmessage
caesar()

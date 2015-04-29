import re

'''
31415;HYEMYDUMPS
45162;M%muxi%dncpqftiix"
14586214;Uix!&kotvx3
'''

if __name__ == '__main__':
	d = list(''' !"#$%&'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz''')
	p = {}
	dl = len(d)
	for i in range(0, dl):
		p[d[i]] = i
	
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		key, text = re.split(';', s)
		key = [int(val) for val in list(key)]
		kl = len(key)
		tl = len(text)
		text = list(text)
		for i in range(0, tl):
			text[i] = d[(p[text[i]] + dl - key[i % kl]) % dl]
		text = ''.join(text)
		print(text)

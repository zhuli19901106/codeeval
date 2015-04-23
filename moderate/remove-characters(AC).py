import re

'''
how are you, abc
hello world, def
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a, b = re.split(', ', s)
		b = list(set(b))
		for val in b:
			a = re.sub('%s+' % val, '', a)
		print(a)

import re

'''
4-2;BEGIN-3;3-4;2-END
4-2;BEGIN-3;3-4;2-3
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a = {}
		for val in re.split(';', s):
			x, y = re.split('-', val)
			a[x] = y
		k = 'BEGIN'
		while True:
			if k == 'END':
				break
			try:
				k1 = a[k]
				del a[k]
				k = k1
			except KeyError:
				break
		print('GOOD' if k == 'END' and len(a) == 0 else 'BAD')

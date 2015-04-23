import re

'''
1 2 3 4
10 -2 3 4
'''

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a = re.split(' ', line)
		b = []
		n = len(a)
		for i in range(n - 1, -1, -2):
			b.append(a[i])
		print(' '.join(b))

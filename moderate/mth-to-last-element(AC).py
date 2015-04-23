import re

'''
a b c d 4
e f g h 2
'''

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a = re.split(' ', line)
		m = int(a.pop())
		n = len(a)
		if m <= n:
			print(a[n - m])

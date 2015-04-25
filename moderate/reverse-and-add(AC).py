import re

def pal(n):
	return str(n) == str(n)[:: -1]

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		n = int(s)
		ans = 0
		while pal(n) == False:
			n = n + int(str(n)[:: -1])
			ans += 1
		print('%d %d' % (ans, n))

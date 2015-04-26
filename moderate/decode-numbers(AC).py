import re

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		s = [int (val) for val in list(s)]
		s.reverse()
		c1 = 1
		c2 = 1 if s[0] > 0 else 0
		n = len(s)
		for i in range(1, n):
			d = s[i] * 10 + s[i - 1]
			c3 = 0
			if s[i] > 0:
				c3 += c2
			if d >= 10 and d <= 26:
				c3 += c1
			c1 = c2
			c2 = c3
		print(c2)

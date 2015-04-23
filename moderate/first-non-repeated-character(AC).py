import re

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		c = {}
		length = len(s)
		for i in range(0, length):
			if c.has_key(s[i]):
				c[s[i]] += 1
			else:
				c[s[i]] = 1
		for i in range(0, length):
			if c[s[i]] == 1:
				print(s[i])
				break

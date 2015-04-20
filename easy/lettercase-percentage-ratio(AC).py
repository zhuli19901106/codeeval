import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		c1 = len(re.findall('[a-z]', line))
		c2 = len(re.findall('[A-Z]', line))
		length = len(line)
		print('lowercase: %.2f uppercase: %.2f' % (100.0 * c1 / length, 100.0 * c2 / length))

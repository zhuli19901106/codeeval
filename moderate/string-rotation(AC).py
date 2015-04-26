import re

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a, b = re.split(',', s)
		a += a
		print(len(a) == 2 * len(b) and a.find(b) != -1)

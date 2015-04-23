import re

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		n = int(s)
		print(bin(n)[2: ])

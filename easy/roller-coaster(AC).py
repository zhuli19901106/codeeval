import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		ans = ''
		length = len(line)
		f = True
		for i in range(0, length):
			if line[i].isalpha():
				if f:
					myprint(line[i].upper())
				else:
					myprint(line[i].lower())
				f = not f
			else:
				myprint(line[i])
		print('')

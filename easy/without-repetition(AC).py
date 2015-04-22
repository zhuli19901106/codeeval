import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		length = len(line)
		i = 0
		while i < length:
			j = i + 1
			myprint(line[i])
			while j < length and line[i] == line[j]:
				j += 1
			i = j
		print('')

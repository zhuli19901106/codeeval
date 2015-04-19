import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		[s, a] = re.split('\|+ +', line)
		a = re.split(' +', a)
		for it in a:
			myprint(s[int(it) - 1])
		print('')
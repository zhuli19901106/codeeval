import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		val = int(float(line) * 3600)
		a = val / 3600
		val %= 3600
		m = val / 60
		val %= 60
		s = val
		print('%d.%02d\'%02d"' % (a, m, s))

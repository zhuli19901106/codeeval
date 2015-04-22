import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a = [int(val) for val in re.split(' ', line)]
		[x1, y1, x2, y2] = a
		if x1 == x2 and y1 == y2:
			print('here')
			continue
		if y2 < y1:
			myprint('S')
		elif y2 > y1:
			myprint('N')
		if x2 < x1:
			myprint('W')
		elif x2 > x1:
			myprint('E')
		print('')

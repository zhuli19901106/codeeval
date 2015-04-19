import math
import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		arr = re.findall('\(.*?\)', line)
		[x1, y1] = re.split(', ', arr[0][1: len(arr[0]) - 1])
		[x2, y2] = re.split(', ', arr[1][1: len(arr[1]) - 1])
		x1 = int(x1)
		x2 = int(x2)
		y1 = int(y1)
		y2 = int(y2)
		ans = int(math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)))
		print('%d' % ans)
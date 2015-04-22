import re
import sys

d = [
[-1, -2], 
[-2, -1], 
[-1, +2], 
[-2, +1], 
[+1, -2], 
[+2, -1], 
[+1, +2], 
[+2, +1], 
]
myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		x = ord(line[0]) - ord('a')
		y = ord(line[1]) - ord('1')
		
		ans = []
		for i in range(0, 8):
			x1 = x + d[i][0]
			y1 = y + d[i][1]
			if x1 < 0 or x1 > 7 or y1 < 0 or y1 > 7:
				continue
			ans.append(chr(x1 + ord('a')) + chr(y1 + ord('1')))
		ans.sort()
		print(' '.join(ans))

import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a = re.split(',', line)
		n = len(a)
		m = len(a[0])
		ans = 1000
		for i in range(0, n):
			bx = False
			px = -1
			for j in range(0, m):
				if a[i][j] == '.':
					continue
				
				if a[i][j] == 'X':
					px = j
					if not bx:
						bx = True
				elif a[i][j] == 'Y':
					if bx:
						ans = min(ans, j - px - 1)
						bx = False
		print(ans)

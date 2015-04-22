import math
import re
import sys

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a = re.split(' ', line)
		n = int(math.sqrt(len(a)))
		c = [[0 for val in range(0, n)] for val in range(0, n)]
		for i in range(0, n):
			for j in range(0, n):
				c[j][n - 1 - i] = a[i * n + j]
		for i in range(0, n):
			for j in range(0, n):
				a[i * n + j] = c[i][j]
		print(' '.join(a))

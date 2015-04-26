import math
import re

'''
4;1,4,2,3,2,3,1,4,4,2,3,1,3,1,4,2
4;2,1,3,2,3,2,1,4,1,4,2,3,2,3,4,1
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		n, a = re.split(';', s)
		n = int(n)
		a = [int(val) - 1 for val in re.split(',', a)]
		
		n2 = n * n
		n1 = int(math.sqrt(n))
		sr = [set() for i in range(0, n)]
		sc = [set() for i in range(0, n)]
		sb = [set() for i in range(0, n)]
		for i in range(0, n2):
			r = i / n
			c = i % n
			b = r / n1 * n1 + c / n1
			sr[r].add(a[i])
			sc[c].add(a[i])
			sb[b].add(a[i])
		suc = True
		for i in range(0, n):
			if len(sr[i]) != n:
				suc = False
				break
			if len(sc[i]) != n:
				suc = False
				break
			if len(sb[i]) != n:
				suc = False
				break
		print(suc)

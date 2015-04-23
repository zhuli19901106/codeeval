import math
import re

'''
5
10
25
3
0
1
'''

if __name__ == '__main__':
	int_max = 2147483647
	sqrt_max = int(math.sqrt(int_max))
	rt = []
	for i in range(0, sqrt_max + 1):
		rt.append(i * i)
	rt = set(rt)
	
	s = raw_input()
	n = int(s)
	for ni in range(0, n):
		s = raw_input()
		x = int(s)
		
		ans = 0
		i = 0
		while i * i <= x - i * i:
			if (x - i * i) in rt:
				ans += 1
			i += 1
		print(ans)

import re

'''
(0,2,4,8,10,13,14,18,22,23,24,33,40,42,44,47,49,53,55,63,66,81,87,91) (0,147,220)
(0,1,2,4) (0,1,3,4,5)
(0,1,3,4,6) (0,1,2,4)
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input().strip()
		except EOFError:
			break
		if len(s) == 0:
			continue
		
		a, b = re.split(' ', s)
		a = [float(val) for val in re.split(',', a[1: len(a) - 1])]
		b = [float(val) for val in re.split(',', b[1: len(b) - 1])]
		a.sort()
		b.sort()
		n = len(a)
		m = len(b)
		r = b[m - 1] / a[n - 1]
		ans = 0
		for i in range(0, n - 1):
			x1 = a[i]
			x2 = a[i + 1]
			y1 = r * x1
			y2 = r * x2
			jl = 0
			while True:
				if jl + 1 == m - 1 or b[jl + 1] > y1:
					break
				else:
					jl += 1
			
			jr = m - 1
			while True:
				if jr - 1 == 0 or b[jr - 1] < y2:
					break
				else:
					jr -= 1
			ans += jr - jl
		print(ans)

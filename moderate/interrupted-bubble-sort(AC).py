import re

'''
36 47 78 28 20 79 87 16 8 45 72 69 81 66 60 8 3 86 90 90 | 1
40 69 52 42 24 16 66 | 2
54 46 0 34 15 48 47 53 25 18 50 5 21 76 62 48 74 1 43 74 78 29 | 6
48 51 5 61 18 | 2
59 68 55 31 73 4 1 25 26 19 60 0 | 2
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a, c = re.split(' \| ', s)
		a = [int(val) for val in re.split(' ', a)]
		c = int(c)
		n = len(a)
		
		ci = 0
		for i in range(0, n - 1):
			for j in range(1, n - i):
				if a[j - 1] <= a[j]:
					continue
				a[j - 1], a[j] = a[j], a[j - 1]
			ci += 1
			if ci >= c:
				break
		print(' '.join([str(val) for val in a]))

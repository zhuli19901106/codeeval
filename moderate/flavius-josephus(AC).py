import re

'''
10,3
5,2
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		n, k = [int(val) for val in re.split(',', s)]
		cc = n
		b = [False for i in range(0, n)]
		ans = []
		
		p = 0
		for i in range(0, n):
			c = 0
			while True:
				if b[p]:
					p = (p + 1) % n
					continue
				c += 1
				if c == k:
					b[p] = True
					ans.append(p)
					cc -= 1
					p = (p + 1) % n
					break
				else:
					p = (p + 1) % n
		print(' '.join([str(val) for val in ans]))

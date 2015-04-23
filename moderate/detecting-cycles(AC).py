import re

'''
2 0 6 3 1 6 3 1 6 3 1
3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49
1 2 3 1 2 3 1 2 3
'''

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a = [int(val) for val in re.split(' ', line)]
		n = len(a)
		suc = False
		for i in range(0, n - 1):
			for j in range(i, n):
				if n - 1 - j < j - i + 1:
					continue
				if (n - i) % (j - i + 1) != 0:
					continue
				k = j + 1
				while k < n:
					if a[k] != a[(k - i) % (j - i + 1) + i]:
						break
					k += 1
				if k == n:
					suc = True
					a = a[i : j + 1]
					break
			if suc:
				break
		a = [str(val) for val in a]
		print(' '.join(a))

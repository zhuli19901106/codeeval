import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a = [int(val) for val in re.split(' ', line)]
		a = a[1 : len(a)]
		n = len(a)
		msum = 1000000000
		for i in range(0, n):
			sum = 0
			for j in range(0, n):
				sum += abs(a[i] - a[j])
			msum = min(msum, sum)
		print(msum)

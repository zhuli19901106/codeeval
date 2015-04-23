import re

'''
-10,2,3,-2,0,5,-15
2,3,-2,-1,10
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a = [int(val) for val in re.split(',', s)]
		
		n = len(a)
		msum = a[0]
		for i in range(1, n):
			msum = max(msum, a[i])
		if msum < 0:
			print(msum)
			continue
		msum = sum = 0
		for i in range(0, n):
			sum += a[i]
			if sum > msum:
				msum = sum
			if sum < 0:
				sum = 0
		print(msum)

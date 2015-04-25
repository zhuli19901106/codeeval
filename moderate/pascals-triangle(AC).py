import re

def next(a):
	n = len(a)
	b = []
	
	b.append(a[0])
	for i in range(1, n):
		b.append(a[i - 1] + a[i])
	b.append(a[n - 1])
	
	return b

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		n = int(s)
		a = [1]
		ans = [] + a
		
		for i in range(1, n):
			a = next(a)
			ans += a
		ans = [str(val) for val in ans]
		print(' '.join(ans))

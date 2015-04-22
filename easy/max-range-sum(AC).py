import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		n, a = re.split(';', line)
		n = int(n)
		a = [int(val) for val in re.split(' ', a)]
		m = len(a)
		if m < n:
			print(0)
			continue
		for i in range(1, m):
			a[i] += a[i - 1]
		ans = max(0, a[n - 1])
		for i in range(n, m):
			ans = max(ans, a[i] - a[i - n])
		print(ans)

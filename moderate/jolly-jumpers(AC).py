import re

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a = re.split(' ', s)
		n = int(a[0])
		a = [int(val) for val in a[1: ]]
		ans = set()
		for i in range(0, n - 1):
			val = abs(a[i + 1] - a[i])
			if val >= 1 and val <= n - 1:
				ans.add(val)
		print('Jolly' if len(ans) == n - 1 else 'Not jolly')

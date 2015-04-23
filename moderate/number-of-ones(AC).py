import re

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		n = int(s)
		ans = 0
		while n != 0:
			n = n & (n - 1)
			ans += 1
		print(ans)

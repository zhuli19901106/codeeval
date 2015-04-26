import re

if __name__ == '__main__':
	a = [5, 3, 1]
	
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		n = int(s)
		ans = 0
		for val in a:
			ans += n / val
			n %= val
		print(ans)

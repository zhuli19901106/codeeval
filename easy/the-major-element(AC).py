import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a = re.split(',', line)
		a = [int(val) for val in a]
		ll = len(a)
		if ll == 0:
			print('None')
			continue
		ans = a[0]
		cc = 1
		for i in range(1, ll):
			if ans == a[i]:
				cc += 1
			else:
				cc -= 1
			if cc == 0:
				ans = a[i]
				cc = 1
		cc = 0
		for i in range(0, ll):
			if a[i] == ans:
				cc += 1
		if cc > ll / 2:
			print(ans)
		else:
			print('None')

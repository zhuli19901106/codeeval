import re

md = dict()
md['Jan'] = 1
md['Feb'] = 2
md['Mar'] = 3
md['Apr'] = 4
md['May'] = 5
md['Jun'] = 6
md['Jul'] = 7
md['Aug'] = 8
md['Sep'] = 9
md['Oct'] = 10
md['Nov'] = 11
md['Dec'] = 12

def count_month(d):
	m, y = re.split(' ', d)
	y = int(y) - 1990
	m = md[m]
	return y * 12 + m

def comp(x, y):
	if x[0] > y[0]:
		return 1
	elif x[0] < y[0]:
		return -1
	elif x[1] > y[1]:
		return 1
	elif x[1] < y[1]:
		return -1
	else:
		return 0

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a = re.split('; ', line)
		a = [[count_month(aii) for aii in re.split('-', ai)] for ai in a]
		length = len(a)
		for i in range(0, length):
			a[i][1] += 1
		a.sort(cmp = comp)
		
		ans = 0
		i = 0
		while i < length:
			rb = a[i][1]
			j = i + 1
			while (j < length and a[j][0] <= rb):
				rb = max(rb, a[j][1])
				j += 1
			ans += rb - a[i][0]
			i = j
		print(ans / 12)

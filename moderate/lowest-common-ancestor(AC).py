import re

'''
8 52
3 29
'''

dep = { 30: 1, 8: 2, 52: 2, 3: 3, 20: 3, 10: 4, 29: 4}
dj = { 10: 20, 29: 20, 3: 8, 20: 8, 8: 30, 52: 30, 30: 30 }

def lca(x, y):
	if dep[x] > dep[y]:
		return lca(y, x)
	while dep[y] != dep[x]:
		y = dj[y]
	while y != x:
		x = dj[x]
		y = dj[y]
	return x

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		x, y = [int(val) for val in re.split(' ', line)]
		print(lca(x, y))

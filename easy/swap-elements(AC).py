import sys

def solve(line):
	[a, b] = line.strip().split(' : ')
	a = [int(ai) for ai in a.split(' ')]
	b = b.split(', ')
	
	for bi in b:
		p1, p2 = bi.split('-')
		p1, p2 = int(p1), int(p2)
		a[p1], a[p2] = a[p2], a[p1]
	return ' '.join((str(ai) for ai in a))

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		print(solve(line))

import re

'''
(1,6), (6,7), (2,7), (9,1)
(4,1), (3,4), (0,5), (1,2)
(4,6), (5,5), (5,6), (4,5)
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
			s = s.strip()
		except EOFError:
			break
		if len(s) == 0:
			continue
		a = re.split(', ', s)
		for i in range(0, 4):
			a[i] = [int(val) for val in re.split(',', a[i][1: len(a[i]) - 1])]
		b = []
		for i in range(0, 4):
			for j in range(i + 1, 4):
				b.append((a[i][0] - a[j][0]) * (a[i][0] - a[j][0]) + (a[i][1] - a[j][1]) * (a[i][1] - a[j][1]))
		b.sort()
		if b[0] > 0 and b[0] == b[1] and b[1] == b[2] and b[2] == b[3] and b[4] == b[5]:
			print('true')
		else:
			print('false')

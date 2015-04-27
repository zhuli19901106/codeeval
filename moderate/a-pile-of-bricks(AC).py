import re

'''
[4,3] [3,-3]|(1 [10,9,4] [9,4,2])
[-1,-5] [5,-2]|(1 [4,7,8] [2,9,0]);(2 [0,7,1] [5,9,8])
[-4,-5] [-5,-3]|(1 [4,8,6] [0,9,2]);(2 [8,-1,3] [0,5,4])
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
		a, b = re.split('\|', s)
		a1, a2 = [eval(val) for val in re.split(' ', a)]
		hx, hy = abs(a1[0] - a2[0]), abs(a1[1] - a2[1])
		if hx > hy:
			hx, hy = hy, hx
		
		b = re.split(';', b)
		n = len(b)
		for i in range(0, n):
			b[i] = [eval(val) for val in re.split(' ', b[i][1: len(b[i]) - 1])]
		
		ans = []
		for val in b:
			val[1][0] = abs(val[1][0] - val[2][0])
			val[1][1] = abs(val[1][1] - val[2][1])
			val[1][2] = abs(val[1][2] - val[2][2])
			val[1].sort()
			if hx >= val[1][0] and hy >= val[1][1]:
				ans.append(val[0])
		ans.sort()
		if len(ans) == 0:
			print('-')
		else:
			print(','.join([str(val) for val in ans]))

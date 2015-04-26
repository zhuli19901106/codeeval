import re

'''
5
9 6
4 6 8
0 7 1 5
'''

if __name__ == '__main__':
	a = []
	n = 0
	
	while True:
		try:
			s = raw_input()
			s = s.strip()
		except EOFError:
			break
		if len(s) == 0:
			continue
		a.append([int(val) for val in re.split(' +', s)])
		n += 1
		
	dp = [[], []]
	dp[0] = [0 for i in range(0, n)]
	dp[1] = [0 for i in range(0, n)]
	dp[0][0] = a[0][0]
	f = 1
	for i in range(1, n):
		nf = (f + 1) % 2
		dp[f][0] = dp[nf][0] + a[i][0]
		dp[f][i] = dp[nf][i - 1] + a[i][i]
		for j in range(1, i):
			dp[f][j] = max(dp[nf][j - 1], dp[nf][j]) + a[i][j]
		f = (f + 1) % 2
	f = (f + 1) % 2
	
	res = dp[f][0]
	for i in range(1, n):
		res = max(res, dp[f][i])
	print(res)

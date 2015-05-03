import re

'''
XMJYAUZ;MZJAWXU
'''

def LCS(a, b):
	if len(set(a) & set(b)) == 0:
		# No letter in common
		return ''
	la = len(a)
	lb = len(b)
	dp = [[0 for j in range(lb + 1)] for i in range(la + 1)]
	for i in range(la):
		for j in range(lb):
			if a[i] == b[j]:
				dp[i + 1][j + 1] = dp[i][j] + 1
			else:
				dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
	max_len = dp[i + 1][j + 1]
	
	c = max_len
	ans = []
	cla = la
	clb = lb
	while c > 0:
		suc = False
		for i in range(c - 1, cla):
			for j in range(c - 1, clb):
				if dp[i + 1][j + 1] == c and a[i] == b[j]:
					suc = True
					cla = i
					clb = j
					ans.append(a[i])
					c -= 1
				if suc:
					break
			if suc:
				break
	ans.reverse()
	
	return ''.join(ans)

if __name__ == '__main__':
	while True:
		try:
			s = raw_input().strip()
		except EOFError:
			break
		if len(s) == 0:
			continue
		a, b = re.split(';', s)
		print(LCS(a, b))

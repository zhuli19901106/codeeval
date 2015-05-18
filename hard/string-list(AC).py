import re

'''
1,aa
2,ab
3,pop
'''

def dfs(s, can, idx, n, ans):
	if idx == n:
		ans.append(''.join(s))
		return
	for i in xrange(len(can)):
		s.append(can[i])
		dfs(s, can, idx + 1, n, ans)
		s.pop()

def main():
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		if len(s) == 0:
			continue
		n, s = re.split(',', s)
		n = int(n)
		s = list(set(s))
		s.sort()
		ans = []
		dfs([], s, 0, n, ans)
		print(','.join(ans))

if __name__ == '__main__':
	main()

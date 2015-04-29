import re

'''
soup,sugar,peas,rice
ljhqi,nrtxgiu,jdtphez,wosqm
cjz,tojiv,sgxf,awonm,fcv
'''

max_chain = 0
s = 0
v = 0

def dfs(idx, chain):
	global max_chain
	global s
	global v
	
	if chain > max_chain:
		max_chain = chain
	for i in range(0, n):
		if v[i] or s[i][0] != s[idx][1]:
			continue
		v[i] = True
		dfs(i, chain + 1)
		v[i] = False

def comp(x):
	return x[2]

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		s = re.split(',', s)
		n = len(s)
		s = [[val[0], val[len(val) - 1]] for val in s]
		for i in range(0, n):
			s[i].append(ord(s[i][0]) * 256 + ord(s[i][1]))
		s.sort(key = comp)
		
		max_chain = 1
		path = []
		i = 0
		while i < n:
			v = [False for val in range(0, n)]
			
			v[i] = True
			dfs(i, 1)
			v[i] = False
			
			j = i + 1
			while j < n and s[j][2] == s[i][2]:
				j += 1
			i = j
		print(max_chain if max_chain > 1 else 'None')

import re

'''
1,2,3,4,6;5
2,4,5,6,9,11,15;20
1,2,3,4;50
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a, sum = re.split(';', s)
		a = [int(val) for val in re.split(',', a)]
		sum = int(sum)
		
		n = len(a)
		res = []
		for i in range(0, n - 1):
			suc = False
			for j in range(i + 1, n):
				if a[i] + a[j] == sum:
					suc = True
					break
			if suc:
				res.append(a[i])
		res = list(set(res))
		res.sort()
		if len(res) == 0:
			print('NULL')
		res = ['%d,%d' % (val, sum - val) for val in res]
		print(';'.join(res))
		
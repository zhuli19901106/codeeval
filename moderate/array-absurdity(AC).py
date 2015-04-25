import re

'''
5;0,1,2,3,0
20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		n, a = re.split(';', s)
		n = int(n)
		a = [int(val) for val in re.split(',', a)]
		for i in range(0, n):
			if a[i] >= 0:
				if a[a[i]] >= 0:
					a[a[i]] = -a[a[i]] - 1
				else:
					print(a[i])
					break
			else:
				if a[-a[i] - 1] >= 0:
					a[-a[i] - 1] = -a[- a[i] - 1] - 1
				else:
					print(-a[i] - 1)
					break

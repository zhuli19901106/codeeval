import re

'''
2,3,1,0,-4,-1
0,-1,3,-2
'''

if __name__ == '__main__':
	cc = 0
	n = 0
	a = []
	
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a = [int(val) for val in re.split(',', s)]
		n = len(a)
		if n < 4:
			print(0)
			continue
		cc = 0
		for i1 in range(0, n):
			for i2 in range(i1 + 1, n):
				for i3 in range(i2 + 1, n):
					for i4 in range(i3 + 1, n):
						if a[i1] + a[i2] + a[i3] + a[i4] == 0:
							cc += 1
		print(cc)

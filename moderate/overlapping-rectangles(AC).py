import re

'''
-3,3,-1,1,1,-1,3,-3
-3,3,-1,1,-2,4,2,2
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a = [int(val) for val in re.split(',', s)]
		b = [max(a[0], a[4]), min(a[1], a[5]), min(a[2], a[6]), max(a[3], a[7])]
		print(b[0] <= b[2] and b[1] >= b[3])

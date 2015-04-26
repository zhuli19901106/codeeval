import re

'''
Center: (2.12, -3.48); Radius: 17.22; Point: (16.21, -5)
Center: (5.05, -11); Radius: 21.2; Point: (-31, -45)
Center: (-9.86, 1.95); Radius: 47.28; Point: (6.03, -6.42)
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a = re.split(';', s)
		c = eval(re.split(':', a[0])[1])
		r = eval(re.split(':', a[1])[1])
		p = eval(re.split(':', a[2])[1])
		if (p[0] - c[0]) * (p[0] - c[0]) + (p[1] - c[1]) * (p[1] - c[1]) < r * r:
			print('true')
		else:
			print('false')

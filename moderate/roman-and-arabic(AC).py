import re

'''
3M1D2C
2I3I2X9V1X
'''

if __name__ == '__main__':
	d = {}
	d['I'] = 1
	d['V'] = 5
	d['X'] = 10
	d['L'] = 50
	d['C'] = 100
	d['D'] = 500
	d['M'] = 1000
	
	while True:
		try:
			s = raw_input().strip('\n ')
		except EOFError:
			break
		n = len(s)
		ans = 0
		for i in range(0, n - 2, 2):
			if d[s[i + 1]] < d[s[i + 3]]:
				ans -= int(s[i]) * d[s[i + 1]]
			else:
				ans += int(s[i]) * d[s[i + 1]]
		ans += int(s[n - 2]) * d[s[n - 1]]
		print(ans)

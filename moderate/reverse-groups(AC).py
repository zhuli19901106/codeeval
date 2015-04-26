import re

'''
1,2,3,4,5;2
1,2,3,4,5;3
'''

def rev(a, ll, rr):
	n = len(a)
	if ll == rr:
		return
	if ll == 0:
		b = a[: rr + 1]
		b.reverse()
		a[: rr + 1] = b
	else :
		a[ll: rr + 1] = a[rr: ll - 1: -1]

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a, k = re.split(';', s)
		a = [int(val) for val in re.split(',', a)]
		k = int(k)
		n = len(a)
		i = 0
		while i + k <= n:
			rev(a, i, i + k - 1)
			i += k
		print(','.join([str(val) for val in a]))

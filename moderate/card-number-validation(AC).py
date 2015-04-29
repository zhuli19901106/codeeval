import re

'''
6011 5940 0319 9511
5537 0213 6797 6815
5574 8363 8022 9735
3044 8507 9391 30
6370 1675 9034 6211 774
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input().strip('\n ')
		except EOFError:
			break
		if len(s) == 0:
			continue
		s = [int(val) for val in list(''.join(re.split(' ', s)))]
		n = len(s)
		i = n - 2
		while i >= 0:
			s[i] *= 2
			i -= 2
		s = list(''.join([str(val) for val in s]))
		sum = 0
		for i in s:
			sum += int(i)
		print('1' if sum % 10 == 0 else '0')

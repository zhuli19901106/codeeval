import re

'''
100 Lower Lower Higher Lower Lower Lower Yay!
948 Higher Lower Yay!
'''

if __name__ == '__main__':
	while True:
		try:
			s = raw_input().strip('\n ')
		except EOFError:
			break
		if len(s) == 0:
			continue
		rr, a = re.split(' ', s, 1)
		rr = int(rr)
		a = re.split(' ', a)
		ll = 0
		for guess in a:
			mm = (ll + rr + 1) / 2
			if guess == 'Lower':
				rr = mm - 1
			elif guess == 'Higher':
				ll = mm + 1
			else:
				ll = rr = mm
				break
		print(mm)

import re

'''
15.94;16.00
17;16
35;35
45;50
'''

d1 = {
'PENNY': .01,
'NICKEL': .05,
'DIME': .10,
'QUARTER': .25,
'HALF DOLLAR': .50,
'ONE': 1.00,
'TWO': 2.00,
'FIVE': 5.00,
'TEN': 10.00,
'TWENTY': 20.00,
'FIFTY': 50.00,
'ONE HUNDRED': 100.00
}

d2 = {}
dk = d1.keys()

def r(x):
	return int(x * 100 + 0.5)

if __name__ == '__main__':
	for k in dk:
		d1[k] = r(d1[k])
		d2[d1[k]] = k
	dk = d2.keys()
	dk.sort(reverse = True)
	
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		x, y = re.split(';', s)
		x = float(x)
		y = float(y)
		x = r(x)
		y = r(y)
		if y < x:
			print('ERROR')
			continue
		elif y == x:
			print('ZERO')
			continue
		y -= x
		res = []
		for k in dk:
			if y / k == 0:
				continue
			res += [k] * (y / k)
			y %= k
		print(','.join([d2[val] for val in res]))

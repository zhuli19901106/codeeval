import re

'''
Higher meaning;Hi mean
this is impossible;im possible
twenty   two minutes;two minutes
Higher meaning;e
'''

def mask(ll):
	return ''.join(['_' for i in range(0, ll)])

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a, b = re.split(';', s)
		a = re.split('\s+', a)
		b = re.split(' ', b)
		ac = len(a)
		bc = len(b)
		i = j = 0
		while i < bc:
			if j == ac:
				break
			r = re.search(b[i], a[j])
			if r != None:
				a[j] = mask(r.start()) + b[i] + mask(len(a[j]) - r.end())
				i += 1
				j += 1
			else:
				a[j] = ''.join(['_' for val in range(0, len(a[j]))])
				j += 1
		while j < ac:
			a[j] = mask(len(a[j]))
			j += 1
		if i < bc:
			print('I cannot fix history')
			continue
		print(' '.join(a))

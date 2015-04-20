import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a, b = re.split(';', line)
		a = re.split(' +', a)
		b = re.split(' +', b)
		length = len(a)
		d = dict()
		for i in range(0, length - 1):
			d[b[i]] = a[i]
		for i in range(1, length + 1):
			if d.has_key(str(i)) == False:
				d[str(i)] = a[length - 1]
				break
		a = []
		for i in range(1, length + 1):
			a.append(d[str(i)])
		print(' '.join(a))

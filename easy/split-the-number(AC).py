import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a, b = re.split(r' ', line)
		c = re.split(r'\+|\-', b)
		ll = [len(ci) for ci in c]
		if b[ll[0]] == '+':
			print('%d' % (int(a[0 : ll[0]]) + int(a[ll[0] : ll[0] + ll[1]])))
		elif b[ll[0]] == '-':
			print('%d' % (int(a[0 : ll[0]]) - int(a[ll[0] : ll[0] + ll[1]])))

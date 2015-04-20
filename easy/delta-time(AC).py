import re

def ts(s):
	a = re.split(':', s)
	return int(a[0]) * 3600 + int(a[1]) * 60 + int(a[2])

def st(t):
	return '%02d:%02d:%02d' % (t / 3600, t % 3600 / 60, t % 60)

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		t1, t2 = re.split(' ', line)
		s1 = ts(t1)
		s2 = ts(t2)
		print(st(max(s1, s2) - min(s1, s2)))

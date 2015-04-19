import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		line = line.strip('; ')
		a = re.split('; ', line)
		a = [int(re.split(',', ai)[1]) for ai in a]
		a.sort()
		length = len(a)
		for i in range(length - 1, 0, -1):
			a[i] -= a[i - 1]
		a = [str(ai) for ai in a]
		print(','.join(a))

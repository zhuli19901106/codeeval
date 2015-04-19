import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		d = dict()
		d['zero'] = 0
		d['one'] = 1
		d['two'] = 2
		d['three'] = 3
		d['four'] = 4
		d['five'] = 5
		d['six'] = 6
		d['seven'] = 7
		d['eight'] = 8
		d['nine'] = 9
		a = re.split(';+', line)
		for ai in a:
			myprint('%d' % d[ai])
		print('')

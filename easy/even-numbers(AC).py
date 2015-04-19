import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		n = int(line[len(line) - 1]) + 1
		print('%d' % (n % 2))
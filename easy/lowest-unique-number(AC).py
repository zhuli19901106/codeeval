import re
import sys

myprint = sys.stdout.write

def find_unique(arr):
	for i in '123456789':
		if arr.count(i) == 1:
			return arr.index(i) + 1
	return 0

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		arr = line.split()
		myprint('%d\n' % find_unique(arr))
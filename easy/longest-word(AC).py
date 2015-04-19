import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a = re.split(' +', line)
		ans = a[0]
		for word in a:
			if (len(word) > len(ans)):
				ans = word
		print(ans)
import re

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a, b = re.split(',', s)
		if len(b) > len(a):
			print(0)
			continue
		if a[len(a) - len(b): len(a)] == b:
			print(1)
		else:
			print(0)

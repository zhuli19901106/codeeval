import re

'''
2
Hello World
CodeEval
Quick Fox
A
San Francisco
'''

if __name__ == '__main__':
	line = raw_input()
	n = int(line)
	a = []
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a.append(line)
		a.sort(key = len, reverse = True)
	for i in range(0, n):
		print(a[i])

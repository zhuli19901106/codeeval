import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		length = len(line)
		if length <= 55:
			print(line)
			continue
		i = 39
		while i >= 0 and line[i] != ' ':
			i -= 1
		i = 40 if i < 0 else i
		print(line[0 : i] + '... <Read More>')

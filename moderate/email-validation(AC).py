import re

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		s = s.strip()
		if s == '':
			continue
		p1 = "^[a-zA-Z0-9]([\\+\\.\\-_][a-zA-Z0-9]|[a-zA-Z0-9])*@[a-zA-Z0-9]([\\.\\-][a-zA-Z0-9]|[a-zA-Z0-9])*?\\.[a-zA-Z0-9]+$"
		p2 = "^\".*?\"@[a-zA-Z0-9]([\\.\\-][a-zA-Z0-9]|[a-zA-Z0-9])*?\\.[a-zA-Z0-9]+$"
		if re.match(p1, s) or re.match(p2, s):
			print('true')
		else:
			print('false')

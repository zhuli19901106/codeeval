import re

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		length = len(s)
		st = []
		b = {')': '(', ']': '[', '}': '{'}
		
		suc = True
		for i in range(0, length):
			if s[i] == '(' or s[i] == '[' or s[i] == '{':
				st.append(s[i])
			elif len(st) > 0 and st[len(st) - 1] == b[s[i]]:
				st.pop()
			else:
				suc = False
				break
		if len(st) > 0:
			suc = False
		print(suc)

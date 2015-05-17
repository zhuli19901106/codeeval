import re

'''
Hello,ell
This is good, is
CodeEval,C*Eval
Old,Young
'''

def main():
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		if len(s) == 0:
			continue
		s, p = re.split(',', s)
		p = re.sub(r'\*', '.*', p)
		p = re.sub(r'\\\.\*', '\\*', p)
		print('true' if re.search(p, s) else 'false')

if __name__ == '__main__':
	main()

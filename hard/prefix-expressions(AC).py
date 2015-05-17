import re

'''
* + 2 3 4
'''

def main():
	calc = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
	TYPE_OP = 0
	TYPE_NUM = 1
	
	while True:
		try:
			s = raw_input().strip()
		except EOFError:
			break
		if len(s) == 0:
			continue
		a = re.split('\s+', s)
		st = []
		tp = []
		for i in xrange(len(a)):
			if a[i] == '+' or a[i] == '*' or a[i] == '/':
				st.append(a[i])
				tp.append(TYPE_OP)
			else:
				st.append(float(a[i]))
				tp.append(TYPE_NUM)
			while True:
				if len(tp) < 3:
					break
				if not (tp[-1] == TYPE_NUM 
				        and tp[-2] == TYPE_NUM and 
						tp[-3] == TYPE_OP):
					break
				n2 = st.pop()
				tp.pop()
				n1 = st.pop()
				tp.pop()
				op = st.pop()
				tp.pop()
				
				st.append(calc[op](n1, n2))
				tp.append(TYPE_NUM)
		tp.pop()
		print(int(st.pop()))

if __name__ == '__main__':
	main()

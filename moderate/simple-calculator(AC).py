from __future__ import division
import re

'''
250*14.3
3^6 / 117
(2.16 - 48.34)^-1
(59 - 15 + 3*6)/21
'''

def main():
	while True:
		try:
			s = raw_input().strip()
		except EOFError:
			break
		s = re.sub('\^', '**', s)
		res = '%.5f' % eval(s)
		if '.' in res:
			res = res.rstrip('0')
		if res[-1] == '.':
			res = res[: -1]
		print(res)

if __name__ == '__main__':
	main()

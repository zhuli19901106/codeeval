import re

'''
A quick brown fox jumps over the lazy dog
A slow yellow fox crawls under the proactive dog
'''

if __name__ == '__main__':
	all = set('abcdefghijklmnopqrstuvwxyz')
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		s = set(s.lower())
		s = list(all - s)
		s.sort()
		if len(s) > 0:
			print(''.join(s))
		else:
			print('NULL')

import re

'''
hat
abc
Zu6
'''

def next_permutation(s):
	n = len(s)
	i = n - 2
	while i >= 0 and s[i] >= s[i + 1]:
		i -= 1
	if i == -1:
		return False
	j = i + 1
	while j < n and s[i] < s[j]:
		j += 1
	j -= 1
	s[i], s[j] = s[j], s[i]
	s1 = s[i + 1: ]
	s1.reverse()
	s[i + 1: ] = s1
	
	return True

if __name__ == '__main__':
	while True:
		try:
			s = raw_input().strip()
		except EOFError:
			break
		if len(s) == 0:
			continue
		a = []
		s = list(s)
		s.sort()
		while True:
			a.append(''.join(s))
			if not next_permutation(s):
				break
		print(','.join(a))

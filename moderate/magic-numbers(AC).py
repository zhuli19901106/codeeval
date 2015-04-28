import re

def is_magic(n):
	n = str(n)
	s = set(n)
	ll = len(n)
	if len(s) < ll:
		return False
	n += n
	i = 0
	while True:
		if not n[i] in s:
			return len(s) == 0 and i == 0
		s.discard(n[i])
		i = (i + int(n[i])) % ll

if __name__ == '__main__':
	while True:
		try:
			s = raw_input().strip()
		except EOFError:
			break
		if len(s) == 0:
			continue
		x, y = [int(val) for val in re.split(' ', s)]
		ans = []
		for i in range(x, y + 1):
			if is_magic(i):
				ans.append(i)
		print(' '.join([str(val) for val in ans]) if len(ans) > 0 else '-1')

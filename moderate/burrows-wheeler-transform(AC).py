'''
oooooooo$  ffffffff     ffffffffuuuuuuuuaaaaaaaallllllllbbBbbBBb|
edarddddddddddntensr$  ehhhhhhhhhhhJ aeaaaaaaaaaaalhtf thmbfe           tcwohiahoJ eeec t e |
ooooio,io$Nnssshhhjo  ee  o  nnkkkkkkii |
'''

def bwt_decode(s, eof):
	lines = ['' for i in range(len(s))]
	for i in range(len(s)):
		for j in range(len(s)):
			lines[j] = s[j] + lines[j]
		lines.sort()
	
	for line in lines:
		if line.endswith(eof):
			return line

if __name__ == "__main__":
	eof = '$'
	
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		s = s[: -1]
		s = bwt_decode(s, eof)
		print(s)

import re

'''
$#**\0100000101101100011100101000
$#**\ 010 00 00 10 11 011 000 111 001 0 1 000
##*\$
'''

if __name__ == '__main__':
	kk = []
	for i in xrange(1, 8):
		for j in xrange((1 << i) - 1):
			kk.append(bin(j)[2: ].zfill(i))
	mm = {}
	
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		if len(s) == 0:
			continue
		i = re.search('[01]', s).start()
		h = s[: i]
		c = s[i: ]
		for i in xrange(len(h)):
			mm[kk[i]] = h[i]
		i = 0
		ans = []
		while True:
			kl = int(c[i: i + 3], 2)
			if kl == 0:
				break
			i += 3
			while True:
				code = c[i: i + kl]
				i += kl
				if code in mm:
					ans.append(mm[code])
				else:
					break
		print(''.join(ans))

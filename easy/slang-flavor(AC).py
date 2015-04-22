import re
import sys

slang = [
', yeah!', 
', this is crazy, I tell ya.', 
', can U believe this?', 
', eh?', 
', aw yea.', 
', yo.', 
'? No way!', 
'. Awesome!'
]
sl = len(slang)

myprint = sys.stdout.write

def check(ch):
	return ch == '.' or ch == '!' or ch == '?'

if __name__ == '__main__':
	idx = 0
	f = False
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		length = len(line)
		for i in range(0, length):
			if check(line[i]):
				if f:
					myprint(slang[idx])
					idx = (idx + 1) % sl
				else:
					myprint(line[i])
				f = not f
			else:
				myprint(line[i])
		print('')

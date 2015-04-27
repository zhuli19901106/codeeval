import re

code = {
    'y' : 'a', 'n' : 'b', 'f' : 'c', 'i' : 'd', 'c' : 'e',
    'w' : 'f', 'l' : 'g', 'b' : 'h', 'k' : 'i', 'u' : 'j',
    'o' : 'k', 'm' : 'l', 'x' : 'm', 's' : 'n', 'e' : 'o',
    'v' : 'p', 'z' : 'q', 'p' : 'r', 'd' : 's', 'r' : 't',
    'j' : 'u', 'g' : 'v', 't' : 'w', 'h' : 'x', 'a' : 'y',
    'q' : 'z', ' ' : ' '
}

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
			s = s.strip('\n ')
		except EOFError:
			break
		s = ''.join([code[val] for val in list(s)])
		print(s)

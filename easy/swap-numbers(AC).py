import re

'''
4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5
5Nobody5 7expects3 5the4 6Spanish4 9inquisition0
'''

def main():
	while True:
		try:
			s = raw_input().strip()
		except EOFError:
			break
		print(' '.join([val[-1] + val[1: -1] + val[0] for val in re.split('\s+', s)]))

if __name__ == '__main__':
	main()
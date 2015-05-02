import re

'''
RIGHT; 4; 4 0 2 0|0 0 0 8|4 0 2 4|2 4 2 2
UP; 4; 2 0 2 0|0 2 0 4|2 8 0 8|0 8 0 16
'''
a = 0
n = 0
d = {'LEFT': +1, 'RIGHT': -1, 'UP': +1, 'DOWN': -1}
dir = 0
start = {}
end   = {}

def print_board():
	global a
	global n
	for val1 in a:
		print(' '.join([str(val2) for val2 in val1]))

def shift():
	global a
	global n
	global d
	global dir
	global start
	global end
	
	if dir == 'LEFT' or dir == 'RIGHT':
		for x in range(0, n):
			c = y = start[dir]
			while y != end[dir] + d[dir]:
				if a[x][y] != 0:
					a[x][c] = a[x][y]
					c += d[dir]
				y += d[dir]
			while c != end[dir] + d[dir]:
				a[x][c] = 0
				c += d[dir]
	else:
		for y in range(0, n):
			c = x = start[dir]
			while x != end[dir] + d[dir]:
				if a[x][y] != 0:
					a[c][y] = a[x][y]
					c += d[dir]
				x += d[dir]
			while c != end[dir] + d[dir]:
				a[c][y] = 0
				c += d[dir]

def merge():
	global a
	global n
	global d
	global dir
	global start
	global end
	
	if dir == 'LEFT' or dir == 'RIGHT':
		for x in range(0, n):
			y = start[dir]
			while y != end[dir]:
				if a[x][y] == 0 or a[x][y] != a[x][y + d[dir]]:
					y += d[dir]
				else:
					a[x][y] *= 2
					a[x][y + d[dir]] = 0
					y += d[dir]
	else:
		for y in range(0, n):
			x = start[dir]
			while x != end[dir]:
				if a[x][y] == 0 or a[x][y] != a[x + d[dir]][y]:
					x += d[dir]
				else:
					a[x][y] *= 2
					a[x + d[dir]][y] = 0
					x += d[dir]

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		dir, n, a = re.split('; ', s)
		n = int(n)
		a = re.split('\|', a)
		for i in range(0, n):
			a[i] = [int(val) for val in re.split(' ', a[i])]
		start['LEFT']  = 0
		start['RIGHT'] = n - 1
		start['UP']    = 0
		start['DOWN']  = n - 1
		
		end['LEFT']  = n - 1
		end['RIGHT'] = 0
		end['UP']    = n - 1
		end['DOWN']  = 0
		
		shift()
		merge()
		shift()
		
		print('|'.join([' '.join([str(val2) for val2 in val1]) for val1 in a]))
		
		start = {}
		end = {}

import re

'''
Hello, World!
The precise 50-digits value of Pi is 3.14159265358979323846264338327950288419716939937510.
But he who would be a great man ought to regard, not himself or his interests, but what is just, whether the just act be his own or that of another. Next as to habitations. Such is the tradition.
'''

'''
Hello, World!
The         precise         50-digits        value        of        Pi        is
3.14159265358979323846264338327950288419716939937510.
But  he  who would be a great man ought to regard, not himself or his interests,
but what is just, whether the just act be his own or that of another. Next as to
habitations. Such is the tradition.
'''

def fill_space(n):
	return ''.join([' ' for val in range(0, n)])

def print_line(a):
	n = len(a)
	if n == 1:
		print(a[0])
		return
	total_len = 0
	for val in a:
		total_len += len(val)
	space_count = 80 - total_len
	space_width = space_count / (n - 1)
	rem = space_count % (n - 1)
	res = ''
	res += a[0]
	for i in range(1, rem + 1):
		res += fill_space(space_width + 1)
		res += a[i]
	for i in range(rem + 1, n):
		res += fill_space(space_width)
		res += a[i]
	print(res)

def process_line(s):
	a = re.split(' ', s)
	ac = len(a)
	
	i = 0
	while i < ac:
		total_len = 0
		wc = 0
		j = i
		while j < ac:
			if total_len + len(a[j]) + wc <= 80:
				total_len += len(a[j])
				wc += 1
				j += 1
			else:
				break
		
		if i == j:
			print(a[i])
			i += 1
		elif j == ac:
			print(' '.join(a[i: j]))
			i = j
		else:
			print_line(a[i: j])
			i = j

if __name__ == '__main__':
	
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		process_line(s)

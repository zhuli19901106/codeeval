import re

def get_one(s):
	length = len(s)
	ans = ''
	for i in range(0, length):
		ans += '1'
	return ans

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a = re.split(' ', line)
		length = len(a)
		ans = ''
		for i in range(0, length, 2):
			if a[i] == '0':
				ans += a[i + 1]
			elif a[i] == '00':
				ans += get_one(a[i + 1])
		print(int(ans, 2))

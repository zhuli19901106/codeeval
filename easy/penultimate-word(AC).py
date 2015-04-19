import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		arr = re.split(' ', line)
		arrLen = len(arr)
		print(arr[arrLen - 2])
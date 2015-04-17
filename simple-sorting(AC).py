import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		arr = re.split(' ', line)
		arrLen = len(arr)
		for i in range(0, arrLen):
			arr[i] = float(arr[i])
		arr.sort()
		for i in range(0, arrLen):
			arr[i] = '%.3f' % arr[i]
		print(' '.join(arr))

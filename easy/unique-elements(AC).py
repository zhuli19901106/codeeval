import re

if __name__ == "__main__":
	arr = list()
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
			
		arr = re.split(',', line)
		arr = list(set(arr))
		arrLen = len(arr)
		for i in range(0, arrLen):
			arr[i] = int(arr[i])
		arr.sort()
		arrLen = len(arr)
		for i in range(0, arrLen):
			arr[i] = str(arr[i])
		print(','.join(arr))

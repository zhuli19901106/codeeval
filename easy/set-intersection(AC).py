import re

def process(str):
	return set(re.split(',', str))

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except:
			break
		arr = re.split(';', line)
		s1 = process(arr[0])
		s2 = process(arr[1])
		s1 = list(s1 & s2)
		arrLen = len(s1)
		if arrLen == 0:
			print('')
			continue
		for i in range(0, arrLen):
			s1[i] = int(s1[i])
		s1.sort()
		for i in range(0, arrLen):
			s1[i] = str(s1[i])
		print(','.join(s1))
		
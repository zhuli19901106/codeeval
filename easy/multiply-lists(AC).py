import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		a1, a2 = re.split(r' \| ', line)
		a1 = re.split(' ', a1)
		a2 = re.split(' ', a2)
		a1 = [int(val) for val in a1]
		a2 = [int(val) for val in a2]
		lengh = len(a1)
		ans = list()
		for i in range(0, lengh):
			ans.append(str(a1[i] * a2[i]))
		print(' '.join(ans))

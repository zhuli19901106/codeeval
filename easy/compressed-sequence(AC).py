import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		line = line.strip(' ')
		a = re.split(' ', line)
		a = [int(ai) for ai in a]
		ans = list()
		length = len(a)
		i = 0
		while i < length:
			j = i + 1
			while j < length and a[i] == a[j]:
				j += 1
			ans.append(j - i)
			ans.append(a[i])
			i = j
		ans = [str(ai) for ai in ans]
		print(' '.join(ans))

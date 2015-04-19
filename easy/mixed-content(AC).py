import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		words = re.findall('[a-z]+', line)
		nums = re.findall('[0-9]+', line)
		words = ','.join(words)
		nums = ','.join(nums)
		if len(words) == 0:
			print(nums)
		elif len(nums) == 0:
			print(words)
		else:
			print(words + '|' + nums)

if __name__ == '__main__':
	ans = [0, 0, 1, 0, 2, 0, 2, 0, 4, 0, 96, 0, 1024, 0, 2880, 0, 81024, 0, 770144]
	while True:
		try:
			s = raw_input().strip(' ')
		except EOFError:
			break
		if len(s) == 0:
			continue
		print(ans[int(s)])

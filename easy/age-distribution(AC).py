import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		age = int(line)
		if age < 0:
			print('This program is for humans')
		elif age < 3:
			print('Still in Mama\'s arms')
		elif age < 5:
			print('Preschool Maniac')
		elif age < 12:
			print('Elementary school')
		elif age < 15:
			print('Middle school')
		elif age < 19:
			print('High school')
		elif age < 23:
			print('College')
		elif age < 66:
			print('Working for the man')
		elif age < 101:
			print('The Golden Years')
		else:
			print('This program is for humans')

import re
import sys

myprint = sys.stdout.write

if __name__ == '__main__':
	a = ['-**----*--***--***---*---****--**--****--**---**--', 
         '*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-', 
         '*--*---*---**---**--****-***--***----*---**---***-', 
         '*--*---*--*-------*----*----*-*--*--*---*--*----*-', 
         '-**---***-****-***-----*-***---**---*----**---**--', 
         '--------------------------------------------------']
	dg = []
	for i in range(0, 6):
		dg.append([])
		for j in range(0, 10):
			dg[i].append(a[i][j * 5 : (j + 1) * 5])
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		ans = []
		for i in range(0, 6):
			ans.append([])
		length = len(line)
		for i in range(0, length):
			if line[i].isdigit() == False:
				continue
			d = int(line[i])
			for j in range(0, 6):
				ans[j].append(dg[j][d])
		
		for i in range(0, 6):
			print(''.join(ans[i]))

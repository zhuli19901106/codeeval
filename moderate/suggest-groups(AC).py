import re

'''
Amira:Isaura,Lizzie,Madalyn,Margarito,Shakira,Un:Driving,Mineral collecting
Elliot:Isaura,Madalyn,Margarito,Shakira:Juggling,Mineral collecting
Isaura:Amira,Elliot,Lizzie,Margarito,Verla,Wilford:Juggling
Lizzie:Amira,Isaura,Verla:Driving,Mineral collecting,Rugby
Madalyn:Amira,Elliot,Margarito,Verla:Driving,Mineral collecting,Rugby
Margarito:Amira,Elliot,Isaura,Madalyn,Un,Verla:Mineral collecting
Shakira:Amira,Elliot,Verla,Wilford:Mineral collecting
Un:Amira,Margarito,Wilford:
Verla:Isaura,Lizzie,Madalyn,Margarito,Shakira:Driving,Juggling,Mineral collecting
Wilford:Isaura,Shakira,Un:Driving
'''

# friends
f = {}
# groups of each friend
fg = {}
# new groups of each friend
nfg = {}
# friends of each group
gf = {}

def should_suggest(group, friend):
	if group in fg[friend]:
		return False
	fc = len(f[friend])
	pc = 0
	for val in f[friend]:
		if not group in fg[val]:
			continue
		pc += 1
	return pc >= (fc + 1) / 2

if __name__ == '__main__':
	
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		name, friends, groups = re.split(':', s)
		
		if name not in f:
			f[name] = set()
		friends = re.split(',', friends)
		for val in friends:
			if val not in f:
				f[val] = set()
			f[name].add(val)
			f[val].add(name)
		
		if name not in fg:
			fg[name] = set()
		if groups == '':
			groups = []
		else:
			groups = re.split(',', groups)
		for val in groups:
			fg[name].add(val)
			if val not in gf:
				gf[val] = set()
			gf[val].add(name)
	
	for val1 in gf.keys():
		cc = 0
		for val2 in f.keys():
			if not should_suggest(val1, val2):
				continue
			if not val2 in nfg:
				nfg[val2] = set()
			nfg[val2].add(val1)
	kk = nfg.keys()
	kk.sort()
	for val in kk:
		ll = list(nfg[val])
		ll.sort()
		print(':'.join([val, ','.join(ll)]))

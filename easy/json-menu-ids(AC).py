import json
import re

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
		except EOFError:
			break
		data = json.loads(line)
		items = data['menu']['items']
		sum = 0
		for item in items:
			if item == None or item.has_key('label') == False:
				continue
			sum += int(item['id'])
		print(sum)

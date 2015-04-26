import re
import urllib

'''
http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html
'''

def get_info(url):
	url = urllib.unquote(url)
	ans = []
	r = re.search('://', url)
	scheme = url[0: r.start()].lower()
	url = url[r.end(): ]
	r = re.search('/', url)
	if r == None:
		host = url
		rest = ''
	else:
		host = url[: r.start()]
		rest = url[r.end(): ]
	r = re.search(':', host)
	if r == None:
		port = 80
	else:
		port = int(host[r.end(): ])
		host = host[: r.start()]
	host = host.lower()
	return [scheme, host, port, rest]

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		a, b = re.split(';', s)
		ia = get_info(a)
		ib = get_info(b)
		print(ia == ib)

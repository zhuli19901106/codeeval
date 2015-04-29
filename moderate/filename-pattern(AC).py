import re

'''
*7* johab.py gen_probe.ko palmtx.h macpath.py tzp dm-dirty-log.h bh1770.h pktloc faillog.8.gz zconf.gperf
*[0123456789]*[auoei]* IBM1008_420.so zfgrep limits.conf.5.gz tc.h ilogb.3.gz limits.conf CyrAsia-TerminusBold28x14.psf.gz nf_conntrack_sip.ko DistUpgradeViewNonInteractive.pyc NFKDQC
*.??? max_user_watches arptables.h net_namespace Kannada.pl menu_no_no.utf-8.vim shtags.1 unistd_32_ia32.h gettext-tools.mo ntpdate.md5sums linkat.2.gz
*.pdf OldItali.pl term.log plymouth-upstart-bridge rand.so libipw.ko jisfreq.pyc impedance-analyzer xmon.h 1.5.0.3.txt bank
g*.* 56b8a0b6.0 sl.vim digctl.h groff-base.conffiles python-software-properties.md5sums CountryInformation.py use_zero_page session-noninteractive d2i_RSAPublicKey.3ssl.gz container-detect.log.4.gz
*[0123456789]* keyboard.h machinecheck 46b2fd3b.0 libip6t_frag.so timer_defs.h nano-menu.xpm NI vim-keys.conf setjmp.h memcg
'''

escape = set('()$+.^{}')

def process_pattern(pat):
	global escape
	
	pat = list(pat)
	ans = []
	n = len(pat)
	i = 0
	ans.append('^')
	while i < n:
		if pat[i] == '?':
			ans.append('.')
			i += 1
		elif pat[i] == '.':
			ans.append('\\')
			ans.append('.')
			i += 1
		elif pat[i] == '*':
			ans.append('.')
			ans.append('*')
			i += 1
		elif pat[i] == '[':
			ans.append('[')
			i += 1
			while pat[i] != ']':
				if pat[i] in escape:
					ans.append('\\')
				ans.append(pat[i])
				i += 1
			ans.append(']')
			i += 1
		else:
			ans.append(pat[i])
			i += 1
	ans.append('$')
	return ''.join(ans)

if __name__ == '__main__':
	while True:
		try:
			s = raw_input()
		except EOFError:
			break
		pat, files = re.split(' ', s, 1)
		pat = process_pattern(pat)
		files = re.split(' ', files)
		ans = []
		for file in files:
			if re.match(pat, file) == None:
				continue
			ans.append(file)
		if len(ans) == 0:
			print('-')
		else:
			print(' '.join(ans))

#include <cctype>
#include <cstdio>
using namespace std;

const int N = 100005;
char s[N];
int cc;

int main()
{
	int i;
	
	while (scanf("%s", s) == 1) {
		cc = 0;
		for (i = 0; s[i]; ++i) {
			if (isdigit(s[i])) {
				putchar(s[i]);
				++cc;
			} else if (s[i] >= 'a' && s[i] <= 'j') {
				putchar(s[i] - 'a' + '0');
				++cc;
			}
		}
		if (cc > 0) {
			putchar('\n');
		} else {
			puts("NONE");
		}
	}
	
	return 0;
}
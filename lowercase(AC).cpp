#include <cstdio>
using namespace std;

const int N = 100005;
char s[N];

int main()
{
	int i;

	while (gets(s) != NULL) {
		for (i = 0; s[i]; ++i) {
			if (s[i] >= 'A' && s[i] <= 'Z') {
				putchar(s[i] - 'A' + 'a');
			} else {
				putchar(s[i]);
			}
		}
		putchar('\n');
	}

	return 0;
}
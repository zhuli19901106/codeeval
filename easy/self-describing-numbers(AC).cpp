#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	char s[1000];
	int c[10];
	int i;
	int len;

	while (scanf("%s", s) == 1) {
		len = strlen(s);
		if (len > 10) {
			printf("0\n");
			continue;
		}

		for (i = 0; i < 10; ++i) {
			c[i] = 0;
		}
		for (i = 0; i < len; ++i) {
			++c[s[i] - '0'];
		}
		for (i = 0; i < len; ++i) {
			if (c[i] != s[i] - '0') {
				break;
			}
		}
		printf("%d\n", i == len ? 1 : 0);
	}

	return 0;
}
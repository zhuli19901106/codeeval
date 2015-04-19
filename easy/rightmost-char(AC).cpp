#include <cstdio>
#include <cstring>
using namespace std;

const int N = 100005;
char s[N];
char ch;
int len;

int main()
{
	char *p;

	while (gets(s) != NULL) {
		len = strlen(s);
		ch = s[len - 1];
		s[len - 2] = 0;
		p = strrchr(s, ch);
		printf("%d\n", p == NULL ? -1 : p - s);
	}

	return 0;
}
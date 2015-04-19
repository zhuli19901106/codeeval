#include <cstdio>
#include <cstring>
using namespace std;

const int N = 100005;
char s[N];

int main()
{
	int i, j, len;
	bool f;

	while (gets(s) != NULL) {
		len = strlen(s);
		while (len > 0 && s[len - 1] == ' ') {
			--len;
		}
		s[len] = 0;

		i = 0;
		while (i < len && s[i] == ' ') {
			++i;
		}

		f = true;
		while (i < len) {
			f ? f = false : putchar(' ');

			if (s[i] >= 'a' && s[i] <= 'z') {
				putchar(s[i] - 'a' + 'A');
			} else {
				putchar(s[i]);
			}

			j = i + 1;
			while (j < len && s[j] != ' ') {
				putchar(s[j++]);
			}
			if (j >= len) {
				break;
			}

			i = j;
			while (i < len && s[i] == ' ') {
				++i;
			}
			if (i >= len) {
				break;
			}
		}
		putchar('\n');
	}

	return 0;
}
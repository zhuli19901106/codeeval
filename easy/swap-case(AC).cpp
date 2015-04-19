#include <cctype>
#include <cstdio>
using namespace std;

const int N = 100005;
char s[N];

int main()
{
	int i;

	while (gets(s) != NULL) {
		for (i = 0; s[i]; ++i) {
			if (islower(s[i])) {
				s[i] = toupper(s[i]);
			} else if (isupper(s[i])) {
				s[i] = tolower(s[i]);
			}
		}
		puts(s);
	}

	return 0;
}
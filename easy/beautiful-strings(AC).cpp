#include <algorithm>
#include <cctype>
#include <cstdio>
using namespace std;

typedef struct Term {
	int idx;
	int cc;
} Term;
Term a[26];

const int N = 100005;
char s[N];
int ans;

bool comp(const Term &t1, const Term &t2)
{
	return t1.cc > t2.cc;
}

int main()
{
	int i;

	while (gets(s) != NULL) {
		for (i = 0; i < 26; ++i) {
			a[i].idx = i;
			a[i].cc = 0;
		}
		for (i = 0; s[i]; ++i) {
			if (islower(s[i])) {
				++a[s[i] - 'a'].cc;
			} else if (isupper(s[i])) {
				++a[s[i] - 'A'].cc;
			}
		}
		sort(a, a + 26, comp);
		ans = 0;
		for (i = 0; i < 26; ++i) {
			ans += a[i].cc * (26 - i);
		}
		printf("%d\n", ans);
	}

	return 0;
}
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
using namespace std;

const int N = 100005;

vector<string> v;
char s[N];
char t[N];
int len;

int main()
{
	int i, j;

	while (gets(s) != NULL) {
		len = strlen(s);
		if (len == 0) {
			// Skip the empty lines.
			continue;
		}

		i = 0;
		while (true) {
			while (i < len && s[i] == ' ') {
				++i;
			}
			if (i >= len) {
				break;
			}
			j = i;
			while (j < len && s[j] != ' ') {
				t[j - i] = s[j];
				++j;
			}
			t[j - i] = 0;
			v.push_back(string(t));
			if (j >= len) {
				break;
			}
			i = j;
		}
		if (v.empty()) {
			continue;
		}
		printf("%s", v.back().data());
		for (i = v.size() - 2; i >= 0; --i) {
			printf(" %s", v[i].data());
		}
		printf("\n");

		v.clear();
	}

	return 0;
}
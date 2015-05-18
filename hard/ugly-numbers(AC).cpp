#include <cstdio>
#include <cstring>
using namespace std;

char s[100];
int n;
int cc;
typedef long long int LL;

void dfs(int idx, int op, LL num, LL sum)
{
	if (idx == n) {
		sum += op * num;
		if (sum % 2 == 0 || sum % 3 == 0 || sum % 5 == 0 || sum % 7 == 0) {
			++cc;
		}
		return;
	}
	
	dfs(idx + 1, op, num * 10 + (s[idx] - '0'), sum);
	dfs(idx + 1, +1, s[idx] - '0', sum + op * num);
	dfs(idx + 1, -1, s[idx] - '0', sum + op * num);
}

int main()
{
	while (gets(s) != NULL) {
		cc = 0;
		n = strlen(s);
		dfs(1, 1, s[0] - '0', 0);
		printf("%d\n", cc);
	}
	
	return 0;
}
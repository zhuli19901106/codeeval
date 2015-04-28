/*
1010 AAAAABBBBAAAA
00 AAAAAA
01001110 AAAABAAABBBBBBAAAAAAA
1100110 BBAABABBA
*/

#include <cstdio>
#include <cstring>
using namespace std;

const int N1 = 155;
const int N2 = 1005;
char s1[N1], s2[N2];
int dp[N1][N2];
int n1, n2;

int main()
{
	int i, j;
	
	while (scanf("%s%s", s1, s2) == 2) {
		n1 = strlen(s1);
		n2 = strlen(s2);
		memset(dp, 0, sizeof(dp));
		dp[0][0] = 1;
		for (i = 0; i < n1; ++i) {
			for (j = 0; j < n2; ++j) {
				if (s1[i] == '0' && s2[j] != 'A') {
					continue;
				}
				if (dp[i][j]) {
					dp[i + 1][j + 1] = 1;
				}
				if (j > 0 && s2[j] == s2[j - 1] && dp[i + 1][j]) {
					dp[i + 1][j + 1] = 1;
				}
			}
		}
		printf(dp[n1][n2] ? "Yes\n" : "No\n");
	}

	return 0;
}
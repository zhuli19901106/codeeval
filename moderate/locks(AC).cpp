#include <cstdio>
#include <cstring>
using namespace std;

const int N = 1005;
int n, m;
int a[N];

int main()
{
	int i, j;
	
	while (scanf("%d%d", &n, &m) == 2) {
		memset(a, 0, sizeof(a));
		for (i = 1; i < m; ++i) {
			for (j = 2; j <= n; j += 2) {
				a[j] = 1;
			}
			for (j = 3; j <= n; j += 3) {
				a[j] = !a[j];
			}
		}
		a[n] = !a[n];
		j = 0;
		for (i = 1; i <= n; ++i) {
			if (a[i] == 0) {
				++j;
			}
		}
		printf("%d\n", j);
	}
	
	return 0;
}
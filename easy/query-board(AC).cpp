#include <cstdio>
#include <cstring>
using namespace std;

const int N = 256;
int a[N][N];
int r[N];
int c[N];
char s[1000];

int main()
{
	int x, y;
	int val;
	int i;

	memset(a, 0, sizeof(a));
	memset(r, 0, sizeof(r));
	memset(c, 0, sizeof(c));
	while (scanf("%s", s) == 1) {
		if (strcmp(s, "SetRow") == 0) {
			scanf("%d%d", &x, &val);
			for (i = 0; i < N; ++i) {
				r[x] += val - a[x][i];
				c[i] += val - a[x][i];
				a[x][i] = val;
			}
		} else if (strcmp(s, "SetCol") == 0) {
			scanf("%d%d", &y, &val);
			for (i = 0; i < N; ++i) {
				r[i] += val - a[i][y];
				c[y] += val - a[i][y];
				a[i][y] = val;
			}
		} else if (strcmp(s, "QueryRow") == 0) {
			scanf("%d", &x);
			printf("%d\n", r[x]);
		} else if (strcmp(s, "QueryCol") == 0) {
			scanf("%d", &y);
			printf("%d\n", c[y]);
		}
	}

	return 0;
}
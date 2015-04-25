#include <cstdio>
#include <cstring>
using namespace std;

const int N = 1000005;
int a[N + 1];
int b[N + 1];
int ac;

void sieve()
{
	int i, j;
	
	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));
	
	b[0] = b[1] = 1;
	for (i = 2; i <= N / i; ++i) {
		if (b[i]) {
			continue;
		}
		for (j = i; j <= N / i; ++j) {
			b[i * j] = 1;
		}
	}
	
	ac = 0;
	for (i = 0; i <= N; ++i) {
		if (!b[i]) {
			a[ac++] = i;
		}
	}
}

int main()
{
	int i;
	int n;

	sieve();
	
	while (scanf("%d", &n) == 1) {
		if (n < 2) {
			continue;
		}
		printf("%d", a[0]);
		for (i = 1; i < ac; ++i) {
			if (a[i] >= n) {
				break;
			}
			printf(",%d", a[i]);
		}
		printf("\n");
	}
	
	return 0;
}
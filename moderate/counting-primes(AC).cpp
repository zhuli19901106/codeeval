#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

const int N = 1000005;
int a[N + 1];
int b[N + 1];

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
	
	a[0] = 0;
	for (i = 1; i <= N; ++i) {
		a[i] = b[i] ? a[i - 1] : a[i - 1] + 1;
	}
}

int main()
{
	int n, m;

	sieve();
	
	while (scanf("%d,%d", &n, &m) == 2) {
		if (n > m) {
			swap(n, m);
		}
		printf("%d\n", a[m] - a[n - 1]);
	}
	
	return 0;
}
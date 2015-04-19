#include <cstdio>
using namespace std;

typedef long long int LL;

LL fib(int n)
{
	if (n <= 0) {
		return 0;
	}
	if (n < 3) {
		return 1;
	}

	int f1, f2, f3;
	int i;

	f1 = f2 = 1;
	for (i = 3; i <= n; ++i) {
		f3 = f1 + f2;
		f1 = f2;
		f2 = f3;
	}
	return f3;
}

int main()
{
	int n;

	while (scanf("%d", &n) == 1) {
		printf("%lld\n", fib(n));
	}

	return 0;
}
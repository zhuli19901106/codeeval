#include <cstdio>
using namespace std;

typedef long long int LL;

int f(LL n)
{
	if (n == 0) {
		return 0;
	}
	
	LL i = 1;
	
	while (i << 1 <= n) {
		i <<= 1;
	}
	return (f(n ^ i) + 1) % 3;
}

int main()
{
	LL n;
	
	while (scanf("%lld", &n) == 1) {
		printf("%d\n", f(n));
	}
	
	return 0;
}
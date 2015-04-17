#include <cstdio>
using namespace std;

int main()
{
	unsigned int x, n;
	unsigned int sum;

	while (scanf("%u,%u", &x, &n) == 2) {
		x &= ~(n - 1u);
		x += n;
		printf("%u\n", x);
	}

	return 0;
}
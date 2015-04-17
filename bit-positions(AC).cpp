#include <cstdio>
using namespace std;

int main()
{
	unsigned int n;
	int p1, p2;

	while (scanf("%u,%d,%d", &n, &p1, &p2) == 3) {
		if (!!(n & (1 << (p1 - 1))) == !!(n & (1 << (p2 - 1)))) {
			puts("true");
		} else {
			puts("false");
		}
	}

	return 0;
}
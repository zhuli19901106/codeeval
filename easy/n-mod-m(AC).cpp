#include <cstdio>
using namespace std;

int main()
{
	int x, y;

	while (scanf("%d,%d", &x, &y) == 2) {
		printf("%d\n", x - x / y * y);
	}

	return 0;
}
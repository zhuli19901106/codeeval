#include <cstdio>
using namespace std;

int x, y, n;

void print(int i)
{
	bool suc;

	suc = false;
	if (i % x == 0) {
		suc = true;
		putchar('F');
	}
	if (i % y == 0) {
		suc = true;
		putchar('B');
	}
	if (!suc) {
		printf("%d", i);
	}
}

int main()
{
	int i;

	while (scanf("%d%d%d", &x, &y, &n) == 3) {
		print(1);
		for (i = 2; i <= n; ++i) {
			putchar(' ');
			print(i);
		}
		putchar('\n');
	}

	return 0;
}
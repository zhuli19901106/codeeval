#include <cstdio>
using namespace std;

int main()
{
	int i, j;

	for (i = 1; i <= 12; ++i) {
		for (j = 1; j <= 12; ++j) {
			printf("%4d", i * j);
		}
		printf("\n");
	}

	return 0;
}
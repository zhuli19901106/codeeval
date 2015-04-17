#include <cstdio>
using namespace std;

int main()
{
	int n;
	int sum;

	while (scanf("%d", &n) == 1) {
		sum = 0;
		while (n > 0) {
			sum += n % 10;
			n /= 10;
		}
		printf("%d\n", sum);
	}

	return 0;
}
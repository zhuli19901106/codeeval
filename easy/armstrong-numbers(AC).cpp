#include <cmath>
#include <cstdio>
using namespace std;

int main()
{
	int n;
	int c;
	int sum;
	int n0;

	while (scanf("%d", &n) == 1) {
		c = log10(1.0 * n) + 1;
		sum = 0;
		n0 = n;
		while (n > 0) {
			sum += pow(n % 10 * 1.0, c);
			n /= 10;
		}
		printf(sum == n0 ? "True\n" : "False\n");
	}

	return 0;
}
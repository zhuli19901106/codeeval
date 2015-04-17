#include <cstdio>
using namespace std;

int main()
{
	long long int n;
	long long int sum;

	sum = 0;
	while (scanf("%lld", &n) == 1) {
		sum += n;
	}
	printf("%lld\n", sum);

	return 0;
}
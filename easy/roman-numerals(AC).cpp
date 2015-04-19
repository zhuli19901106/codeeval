#include <cstdio>
using namespace std;

int main()
{
	int n;
	int i, d;
	char hundred[9][5] = {"C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
	char ten[9][5] = {"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
	char one[9][5] = {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
	
	while (scanf("%d", &n) == 1) {
		d = n / 1000;
		if (d > 0) {
			d = n / 1000;
			for (i = 1; i <= d; ++i) {
				putchar('M');
			}
		}
		d = n % 1000 / 100;
		if (d > 0) {
			printf(hundred[d - 1]);
		}
		d = n % 100 / 10;
		if (d > 0) {
			printf(ten[d - 1]);
		}
		d = n % 10;
		if (d > 0) {
			printf(one[d - 1]);
		}
		putchar('\n');
	}
	
	return 0;
}
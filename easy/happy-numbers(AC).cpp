#include <cstdio>
#include <unordered_set>
using namespace std;

int sum(int n)
{
	int s = 0;
	while (n > 0) {
		s += (n % 10) * (n % 10);
		n /= 10;
	}
	return s;
}

int main()
{
	unordered_set<int> us;
	unordered_set<int>::iterator it;
	int n;

	while (scanf("%d", &n) == 1) {
		while (n != 1) {
			if (us.find(n) != us.end()) {
				break;
			}
			us.insert(n);
			n = sum(n);
		}
		if (n == 1) {
			printf("1\n");
		} else {
			printf("0\n");
		}
		us.clear();
	}

	return 0;
}
#include <algorithm>
#include <cstdio>
using namespace std;

int len, d, n;
vector<int> p;
int ans;

int main()
{
	int i;
	
	while (scanf("%d%d%d", &len, &d, &n) == 3) {
		if (n == 0) {
			ans = max((len - 12) / d + 1, 0);
			printf("%d\n", ans);
			continue;
		}
		
		p.resize(n);
		for (i = 0; i < n; ++i) {
			scanf("%d", &p[i]);
		}
		sort(p.begin(), p.end());
		ans = 0;
		for (i = 0; i < n - 1; ++i) {
			ans += (p[i + 1] - p[i]) / d - 1;
		}
		if (p[0] > 6) {
			ans += (p[0] - 6) / d;
		}
		if (p[n - 1] < len - 6) {
			ans += (len - 6 - p[n - 1]) / d;
		}
		printf("%d\n", ans);
		
		p.clear();
	}

	return 0;
}
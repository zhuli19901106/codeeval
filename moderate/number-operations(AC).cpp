/*
44 6 1 49 47
34 1 49 2 21
31 38 27 51 18
*/
#include <cstdio>
using namespace std;

bool suc;

void getNext(int a[], int b[], int i, int j, int n, int sum)
{
	int k, c;
	
	c = 0;
	b[c++] = sum;
	for (k = 0; k < n; ++k) {
		if (k == i || k == j) {
			continue;
		}
		b[c++] = a[k];
	}
}

void dfs(int a[], int n, int idx)
{
	int sum;
	
	if (suc) {
		return;
	}
	
	if (n == 1) {
		if (a[0] == 42) {
			suc = true;
		}
		return;
	}
	
	int i, j;
	int b[5];
	
	if (idx == -1) {
		for (i = 0; i < n; ++i) {
			for (j = i + 1; j < n; ++j) {
				sum = a[i] + a[j];
				getNext(a, b, i, j, n, sum);
				dfs(b, n - 1, 0);
				
				sum = a[i] - a[j];
				getNext(a, b, i, j, n, sum);
				dfs(b, n - 1, 0);
				
				sum = a[j] - a[i];
				getNext(a, b, i, j, n, sum);
				dfs(b, n - 1, 0);
				
				sum = a[i] * a[j];
				getNext(a, b, i, j, n, sum);
				dfs(b, n - 1, 0);
			}
		}
	} else {
		for (i = 1; i < n; ++i) {
			sum = a[0] + a[i];
			getNext(a, b, 0, i, n, sum);
			dfs(b, n - 1, 0);
			
			sum = a[0] - a[i];
			getNext(a, b, 0, i, n, sum);
			dfs(b, n - 1, 0);
			
			sum = a[0] * a[i];
			getNext(a, b, 0, i, n, sum);
			dfs(b, n - 1, 0);
		}
	}
}

int main()
{
	int a[5];
	int i;
	
	while (scanf("%d", &a[0]) == 1) {
		for (i = 1; i < 5; ++i) {
			scanf("%d", &a[i]);
		}
		suc = false;
		dfs(a, 5, -1);
		printf(suc ? "YES\n" : "NO\n");
	}

	return 0;
}
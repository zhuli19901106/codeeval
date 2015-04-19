#include <cstdio>
#include <string>
#include <vector>
using namespace std;

char s[100];
vector<string> a;
vector<int> c, g;
int n;

int main()
{
	int i;
	
	n = 0;
	while (scanf("%s", s) == 1) {
		++n;
		a.push_back(string(s));
		c.push_back(-1);
		g.push_back(-1);
		for (i = 0; s[i]; ++i) {
			if (s[i] == '_') {
				g.back() = i;
			} else if (s[i] == 'C') {
				c.back() = i;
			}
		}
	}
	
	int pos = g[0];
	
	a[0][pos] = '|';
	for (i = 1; i < n; ++i) {
		if (c[i] != -1) {
			if (c[i] < pos) {
				a[i][c[i]] = '/';
			} else if (c[i] > pos) {
				a[i][c[i]] = '\\';
			} else {
				a[i][c[i]] = '|';
			}
			pos = c[i];
		} else {
			if (g[i] < pos) {
				a[i][g[i]] = '/';
			} else if (g[i] > pos) {
				a[i][g[i]] = '\\';
			} else {
				a[i][g[i]] = '|';
			}
			pos = g[i];
		}
	}
	
	for (i = 0; i < n; ++i) {
		puts(a[i].data());
	}
	
	a.clear();
	c.clear();
	g.clear();
	
	return 0;
}
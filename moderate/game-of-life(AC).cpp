#include <cstdio>
#include <cstring>
using namespace std;

const int N = 105;
const int IC = 10;
char a[N][N];
char b[N][N];
int n;
int d[8][2] = {
	{-1, -1}, 
	{-1,  0}, 
	{-1, +1}, 
	{ 0, -1}, 
	{ 0, +1}, 
	{+1, -1}, 
	{+1,  0}, 
	{+1, +1}
};

void nextState()
{
	int x, y, x1, y1;
	int i;
	int nc;
	
	for (x = 0; x < n; ++x) {
		for (y = 0; y < n; ++y) {
			nc = 0;
			for (i = 0; i < 8; ++i) {
				x1 = x + d[i][0];
				y1 = y + d[i][1];
				if (x1 < 0 || x1 > n - 1 || y1 < 0 || y1 > n - 1) {
					continue;
				}
				if (a[x1][y1] == '*') {
					++nc;
				}
			}
			if (a[x][y] == '.') {
				b[x][y] = nc == 3 ? '*' : '.';
			} else {
				b[x][y] = nc >= 2 && nc <= 3 ? '*' : '.';
			}
		}
	}
	memcpy(a, b, sizeof(a));
}

void printState()
{
	int i;
	
	for (i = 0; i < n; ++i) {
		puts(a[i]);
	}
}

int main()
{
	int i;
	
	scanf("%s", a[0]);
	n = strlen(a[0]);
	for (i = 1; i < n; ++i) {
		scanf("%s", a[i]);
	}
	for (i = 0; i < IC; ++i) {
		nextState();
	}
	
	printState();

	return 0;
}
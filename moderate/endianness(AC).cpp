#include <cstdio>
using namespace std;

typedef union {
	unsigned u;
	char c[4];
} Endian;

int main()
{
	Endian e;

	e.c[0] = 1;
	e.c[1] = 0;
	e.c[2] = 0;
	e.c[3] = 0;
	printf(e.u == 1u ? "LittleEndian\n" : "BigEndian\n");
	
	return 0;
}
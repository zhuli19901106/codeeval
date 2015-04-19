#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
	ifstream fin(argv[1]);
	streampos pos;

	fin.seekg(0, ios::end);
	pos = fin.tellg();
	cout << pos << endl;
	fin.close();

	return 0;
}
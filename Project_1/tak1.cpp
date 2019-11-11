#include <iostream>

using namespace std;

int function3(int);
void function2(int);


int function1(int x){
		int i=3;
		int k = 2;
		cout << &i<<endl;
		cout << &k<<endl;
		cout << i +k;
		int f = 3;
		function2(f);
		return f;
	}

void function2(int f){
		int a = 3;
		int b = 2;
		cout << &a<<endl;
		cout << &b<<endl;
		cout << a<<"WHOA!"<<b+f;
		function3(a);
	}

int function3(int n){
		int c = 3;
		int d = 2;
		cout << "funkytown"<< c+d+n;
		return 0;
	}
	


int main(){
	
	int x = 1;

	int q = function1(x);
	cout << q;
	return 0;


}


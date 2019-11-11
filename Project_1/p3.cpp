#include <iostream>
#include <limits.h>
#include <stdlib.h>
#include <cmath>
using namespace std;

int main(){
	
	int x, y, div, addition, multiplication;
	
	cout << "Give me two numbers" << endl;
	cin >> x;
	cin >> y;

	if ((y>0) && (x > INT_MAX - y)){   //if x is bigger than int_max - y, then there would be an overflow (and everything else would break too)
		cout << "BAD!";
		return -1;
	}
	else if ((y<0) && (x < INT_MIN - y)){  //same thing as above but for the other end
		cout << "Underflow";
		return -1;
	}

	addition = x+y;
	cout << "Addition:" << addition << endl;
	
	if ( (y && x != 0) && (abs(x) > INT_MAX / abs(y))){  //first check to make sure both x and y arnt 0, because that situation can never overflow (break). Then check that x is greater than int_max / y else there will be overflow
		cout<< "Overflow";			//needed to use abs() because negatives were breaking it, need only one check this way as well 
		return -1;
	}
	
	multiplication = x * y;
	cout << "Mult:" << multiplication<< endl;
	
	if ( y == 0){			//just need to check for divide by 0 
		cout << "Divide by 0";
		return -1;
	}
	else{
		div = x / y;
		cout << "Div:" << div << endl;
	}

		
	return 0;
	
}

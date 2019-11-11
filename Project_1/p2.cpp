

#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
	
	int locstat[10];

	printf("Address of locstat %p \n", &locstat); //address of first value
	printf("Address of last value in locstat is %p \n", &locstat[9]); //address of last value
	int* locdyn = new int[50];

	printf("Address of locdyn %p \n", &locdyn);
	delete[] locdyn;

}

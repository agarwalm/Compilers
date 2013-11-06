// Mrigya Agarwal, Giuseppe Mendola, Christine Graff

#include <stdio.h>

int input ()
{
	int n;
	scanf("%d", &n);
	return n;
}

int print_int_nl(int x){
	if ((x&3) == 0){
		int temp = x>>2;
		printf("%d\n",temp);
	}
	else{
		int temp = x>>2;
		if(temp == 0){
			printf("%s\n","False");
		}
		else{
			printf("%s\n","True");
		}
	}
	return 0;
}


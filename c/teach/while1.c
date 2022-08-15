#include <stdio.h>

int main(void){
	int i = 0, sum = 0;
	while (i < 5){
		sum = sum + i;
		i++;
		printf("\n%d = %3d", i, sum);
	}
	return 0;
}

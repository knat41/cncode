#include <stdio.h>

int data[10] = {8, 7, 9, 10, 1, 3, 5, 4, 6, 2};

void showdata(void){
	for(int i = 0; i < 10; i++){
		printf("%d ", data[i]);
	}
}
int main(void){
	// find minimum data in data array
	int min = data[0], loc;
	for(int i = 0; i < 10; i++){
		if(min > data[i]){
			min = data[i]; 
			loc = i;
		}
	}
	showdata();
	printf("min = %d location = %d", min, loc);
	return 0;
}
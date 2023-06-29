#include <stdio.h>

int data[10] = {8, 7, 9, 10, 1, 3, 5, 4, 6, 2};

void showdata(void){
	printf("\n");
	for(int i = 0; i < 10; i++){
		printf("%d ", data[i]);
	}
}
int main(void){
	int min = data[0], loc, tmp;
	
	for(int i = 0; i < 9; i++){
		// find minimum data in data array
		for(int j = i + 1; j < 10; j++){
			if(min > data[j]){
				min = data[j];
				loc = j;
			}
		}
		if(data[i] > data[loc]){
			tmp = data[i];
			data[i] = data[loc];
			data[loc] = tmp;
		}
		min = data[i + 1];
		showdata();				
	}	
	
	printf("min = %d location = %d", min, loc);
	return 0;
}
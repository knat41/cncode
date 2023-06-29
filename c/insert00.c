#include <stdio.h>

int data[10] = {8, 7, 9, 10, 1, 3, 5, 4, 6, 2};

void showdata(void){
	printf("\n");
	for(int i = 0; i < 10; i++){
		printf("%d ", data[i]);
	}
}
int main(void){
	
	int i, j, v;
	
	for(i = 1; i < 10; i++){
		v = data[i];
		j = i - 1;
		while((j >= 0) && (data[j] > v)){
			data[j + 1] = data[j];
			j = j - 1;			
		}
		data[j + 1] = v;
		showdata();
	}
	
	return 0;
}
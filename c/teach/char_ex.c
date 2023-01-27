#include <stdio.h>
#include <string.h>

int main(void){
	int a = 0, b = 0, k;
	char *j;
	char *names[] = {"Acer", "Canon", "Veriton"};
	for(int i = 0; i < 3; i++){
		printf("%s\n", names[i]);
		for(j = names[i], k = 0; k < strlen(names[i]); k++){
			printf("%c", *j++);
		}
	}

	return 0;
}
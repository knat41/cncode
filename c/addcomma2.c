/**********************
 * Program : Add Comma in Thousand
 * Writer  : NAT KANJANASIRI
 * Date    : Jan 30, 2023
 * Version : 0.15
 **********************/
#include <stdio.h>
#include <string.h>

int main (){
  char buffer[50], answer[50] = "";  
  long remainder, number;
  scanf("%d", &number);
  while(number > 0){
	remainder = number % 1000;
	number = number / 1000;
	strcpy(buffer, answer);
	if(number > 0 && remainder == 0){
		sprintf (answer, ",000%s", buffer);
	} else if(number > 0 && remainder != 0){
		sprintf (answer, ",%d%s", remainder, buffer);
	} else{
		sprintf (answer, "%d%s", remainder, buffer);
	}
  }
  printf ("%s\n", answer);
  return 0;
}
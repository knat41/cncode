#include <stdio.h>

#define FixCost 5
#define BaseCost 2

int main(void){
	char size, ispepperoni, ischeese, ismushroom;
	float price, cost, area, diameter, extracost;
	printf("Welcome to My Pizza Shop!!\n");
	printf("--------------------------\n");
	printf("Enter pizza size (s, m or l) :");
	scanf("%c", &size);
	printf("Extra pepperoni (y/n) ?:");
	scanf("%s", &ispepperoni);	
	printf("Extra cheese (y/n) ?:");
	scanf("%s", &ischeese);	
	printf("Extra mushroom (y/n) ?:");
	scanf("%s", &ismushroom);	
	if (size == 's')
		diameter = 10.0;
	else if (size == 'm')
		diameter = 16.0;
	else if (size == 'l')
		diameter = 20.0;
	area = (22 / 7) * (diameter * diameter) / 4;
	if (ispepperoni == 'y')
		extracost = 0.50;
	else if (ischeese == 'y')
		extracost = 0.25;
	else if (ismushroom == 'y')
		extracost = 0.30;
	
	cost = FixCost + (BaseCost * area) + (extracost * area);
	price = 1.5 * cost;
	printf("area = %.2f cost = %.2f", area, cost);
	printf("\n--------------------------\n");
	printf("Your order costs %.2f\n", price);
	printf("Thank you");

	return 0;
}

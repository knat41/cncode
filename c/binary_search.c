  
/**********************
 * Program : binary search
 * Writer  : NAT KANJANASIRI
 * Date    : Aug 5, 2022
 * Version : 0.12
 **********************/
#include <stdio.h>

int main(void){
	int found = 0;	int target = 100; int left = 0; int right = 17;
	int mid, x; int nc = 1;
	int A[18] = {8, 9, 13, 35, 42, 44, 50, 54, 58, 60, 61, 62, 77, 84, 86, 90, 92, 96};
	while (left <= right) {
		mid = (left + right) / 2;
		x = A[mid];
		printf("ROUND %d LEFT = %d RIGHT = %d MID = %d " , nc, left + 1, right + 1, mid +1);
		if (x == target){
			found = 1;
			printf("%d equal to %d\n", x, target);
			break;
		}
		if (x < target){
			left = mid + 1;
			printf("%d less than %d\n", x, target);
		}
		if (x > target){
			right = mid - 1;
			printf("%d greater than %d\n", x, target);
		}
		nc++;
	}
	(found == 1) ? printf("found %d at %d", x, mid + 1) :  printf("not found ");
	return 0;
}

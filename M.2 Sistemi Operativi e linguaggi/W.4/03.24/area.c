#include <stdio.h>
#include <math.h>
	
/*
* Programma per calcolare area di un Quadrato, di un Triangolo equilaterlo e di un cerchio a partire  da un numero reale D
*/

int main (){
	float d;

	printf("Inserisci un numero reale D: ");
	scanf("%f", &d);

	//calcola e stampa l'area del quadrato di lato D
	float area_quadrato = d * d;
	printf("L'area del quadrato di lato %f è %f\n",d, area_quadrato);

	//calcola e stampa l'area del cerchio di diametro D
	float r = d /2;
	float area_cerchio = M_PI * r * r;
	printf("L'area del cerchio di diametro %f è  %f\n", d, area_cerchio);

	//calcola e stampa l'area del triangolo  equilatero di lato D
	float altezza = sqrt(3) / 2 * d;
	float area_triangolo = d * altezza / 2;
	printf("L'area del triangolo equilatero di lato %f è %f\n", d, area_triangolo);

	return 0;

}



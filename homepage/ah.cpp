#include<stdio.h>
main()
{
void display(int);
	int i,j;
	int a[]={45,48,78};
	for(i=0;i<5;i++)
	{
		for (j=0;j<i;j++)
		{
		printf("*");
	    }
	  printf("\n");
	}
}
void display(int m)
{
printf("%d",m);
}


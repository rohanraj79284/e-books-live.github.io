#include<stdio.h>
#include<conio.h>
main()
{
	int i,j,arr[3][3],h;
	for(i=0;i<4;i++)
	for(j=0;j<4;j++)
	{
		printf("enter the values %d %d ",i,j);
		scanf("%d",&arr[i][j]);
		printf("%d",arr[i][j]);
	}
}


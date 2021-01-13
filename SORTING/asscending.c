#include<stdio.h>
int main()

{
	int a[100],i,j,k,n;
	printf("Enter the number of elements");
	scanf("%d",&n);
	printf("Enter the elements");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("Ascending order ");
	for(j=0;j<n;j++)
	{
	
	for(i=0;i<n;i++)
	{
	
	if(a[i]>a[j+1])
	{
		k=a[i];
		a[i]=a[j+1];
		a[j+1]=k;
		
	}
}
}
for(i=1;i<=n;i++)
{
printf("%d\t",a[i]);
}
}

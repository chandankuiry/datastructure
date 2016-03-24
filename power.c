#include<stdio.h>
#include<conio.h>

int power1(int base,int exp)
{
	int temp,ans;
	if(exp==0)
		return 1;
	/*else if(exp==2)
		return base*base;*/
	temp=power1(base,exp/2);
	
		if(exp%2==0)
		{
			return temp*temp;
		}
		else
		{
			return base*temp*temp;
		}
}
int main()
{
	int base,exponent,ans;
	printf("Enter the base::");
	scanf("%d",&base);
	printf("\nEnter the exponent::");
	scanf("%d",&exponent);
	ans=power1(base,exponent);
	printf("%d to the power %d is :: %d",base,exponent,ans);
	return 0;
}

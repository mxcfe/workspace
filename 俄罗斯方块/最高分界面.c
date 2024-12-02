#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <time.h>
#define UP 2
#define DOWN 28
#define LIFT 14
#define RIGHT 48
		
extern int flag,fs,zgf,TIME,a[100][30],b[100][30];

typedef struct
{
	int x;
	int y;
}zb;
		
int fun3(int zgf)
{
	int i,j,n;
	system("cls");
	for(i=1;i<=10;i++)
	{
		gotoxy(13,3+i);
		color(14);
		if(i==1)
			printf("--------------------最高分-------------------");
		else if(i==10)
			for(j=1;j<=45;j++)
			{
					printf("-");
				
			}
		else
			for(j=1;j<=45;j++)
			{
				if(j==1||j==43)
					printf("::");
				else
					printf(" ");
				
			}
	}
	color(12);
	gotoxy(35,8);
	printf("%d",zgf);
		color(12);
	gotoxy(20,10);
		printf("1.返回主菜单");
	gotoxy(40,10);
		printf("2.分数归零");
	gotoxy(15,15); 
	color(3);
	printf("请选择[1 2]:[ ]\b\b"); 
	scanf("%d",&n);
	return n;
} 

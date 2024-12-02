#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <time.h>
#define UP 2
#define DOWN 28
#define LIFT 14
#define RIGHT 48

extern int flag,fs,zgf,CS,TIME,a[100][30],b[100][30];

int zjm()		
{
	int i,j,n;
	system("cls");
	color(15);
	gotoxy(26,3);
	printf(" 俄 罗 斯 方 块"); 
	
	color(3);
	gotoxy(18,5);
	printf("■"); 
	gotoxy(18,6);
	printf("■■"); 
	gotoxy(18,7);
	printf("■"); 
	
	color(6);
	gotoxy(25,6);
	printf("■■"); 
	gotoxy(27,7);
	printf("■■"); 
	
	color(10);
	gotoxy(33,6);
	printf("■■"); 
	gotoxy(33,7);
	printf("■■"); 
	
	color(13);
	gotoxy(40,5);
	printf("■"); 
	gotoxy(40,6);
	printf("■"); 
	gotoxy(40,7);
	printf("■");
 	gotoxy(40,8);
	printf("■"); 
	
	color(14);
	gotoxy(49,6);
	printf("■"); 
	gotoxy(45,7);
	printf("■■■"); 
	color(15);

	for(i=1;i<=10;i++)
	{
		gotoxy(13,8+i);
		color(14);
		if(i==1||i==10)
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
		printf("\n");
	}
	
	gotoxy(21,12);
	color(12);
	printf("1.开始游戏");
	gotoxy(39,12);
	printf("2.游戏说明");
	gotoxy(21,15);
	printf("3.最高分");
	gotoxy(39,15);
	printf("4.退出");
	
	
	color(3);
	if(CS==1)
	{
		gotoxy(35,20);
		printf("当前为测试模式"); 

	}
	gotoxy(15,20);
	printf("请选择[1 2 3 4]:[ ]\b\b"); 
	color(14);
	scanf("%d",&n);
	return n;
}


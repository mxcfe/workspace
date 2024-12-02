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

int js(i,n)
{
	int x,cnt=0;
	int xdwz[6];
	zb xy1[6];
	if(n<=LIFT+2&&(i==2||i==3||i==4||i==5))
		n=LIFT+4;
	if(n>=RIGHT-2&&(i==0||i==2||i==3||i==4||i==6))
		n=RIGHT-4;
	xy1[0].x=n;
	switch(i)
	{
		case 0:xy1[0].y=3;xdwz[0]=2;xdwz[1]=0;xdwz[2]=0;xdwz[3]=1;xdwz[4]=2;xdwz[5]=1;
				break;
		case 1:xy1[0].y=5;xdwz[0]=2;xdwz[1]=-2;xdwz[2]=0;xdwz[3]=-1;xdwz[4]=0;xdwz[5]=1;
				break;
		case 2:xy1[0].y=4;xdwz[0]=-2;xdwz[1]=-1;xdwz[2]=0;xdwz[3]=-1;xdwz[4]=2;xdwz[5]=0;
				break;
		case 3:xy1[0].y=4;xdwz[0]=2;xdwz[1]=-1;xdwz[2]=0;xdwz[3]=-1;xdwz[4]=-2;xdwz[5]=0;
				break;
		case 4:xy1[0].y=4;xdwz[0]=-2;xdwz[1]=0;xdwz[2]=0;xdwz[3]=-1;xdwz[4]=2;xdwz[5]=0;
				break;
		case 5:xy1[0].y=4;xdwz[0]=-2;xdwz[1]=-1;xdwz[2]=0;xdwz[3]=-1;xdwz[4]=0;xdwz[5]=1;
				break;
		case 6:xy1[0].y=4;xdwz[0]=2;xdwz[1]=-1;xdwz[2]=0;xdwz[3]=-1;xdwz[4]=0;xdwz[5]=1;
				break;
	}
		xy1[1].x=xy1[0].x+xdwz[0];
		xy1[1].y=xy1[0].y+xdwz[1];
		xy1[2].x=xy1[0].x+xdwz[2];
		xy1[2].y=xy1[0].y+xdwz[3];
		xy1[3].x=xy1[0].x+xdwz[4];
		xy1[3].y=xy1[0].y+xdwz[5];

		if(pd(xy1)==0)
				return 0;
	return 1;
}

int jsjm()                                
{
	int i,j,n;
	system("cls");
	for(i=1;i<=10;i++)
	{
		gotoxy(13,3+i);
		color(14);
		if(i==1)
			printf("-------------------游戏结束------------------");
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
	gotoxy(20,7);
	if(zgf==fs)
		printf("恭喜，您的成绩为目前最高分：%d ",fs);
	else
		printf("目前最高分为：%d，您的成绩为：%d",zgf,fs);
	gotoxy(20,10);
		printf("1.再来一局");
	gotoxy(40,10);
		printf("2.返回主菜单");
	gotoxy(15,15); 
	color(3);
	printf("请选择[1 2]:[ ]\b\b"); 
	scanf("%d",&n);
	return n;
} 


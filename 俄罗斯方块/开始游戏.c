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

int yxzjm()					 
{
	int i,j;
	system("cls");
	gotoxy(27,1);
	color(11);
	printf("俄罗斯方块");
	color(12);
	for(i=UP;i<=DOWN;i++)
	{
		gotoxy(LIFT,i);
		if(i==UP||i==DOWN)
		{
			for(j=LIFT;j<=RIGHT;j++)
			{
				if(i==UP&&j==LIFT)
					printf("┏");
				else if(i==UP&&j==RIGHT)
					printf("┓");
				else if(i==DOWN&&j==LIFT)
					printf("┗");
				else if(i==DOWN&&j==RIGHT)
					printf("┛");
				else
					printf("━");
			}
		}
		else
			for(j=LIFT;j<=RIGHT;j++)
			{
				if(j==LIFT||j==RIGHT)
					printf("┃");
				else
					printf(" ");
			}
		printf("\n");
	}
		 
	gotoxy(55,10);
	color(10);
	printf("**********");
	gotoxy(55,20);
	printf("**********");
	
	gotoxy(55,5);
	color(14);
	printf("目前得分：0");
	gotoxy(55,7);
	printf("目前下落速度：1000ms");
	
	gotoxy(65,10);
	color(3);
	printf("下一个方块：");
	gotoxy(55,21);
	color(14); 
	printf("Esc：退出游戏");
	gotoxy(55,22);
	printf("↑键：变换");
	gotoxy(55,23);
	printf("空格：暂停游戏");
	gotoxy(55,24);
	color(13);
	printf("游戏已开始");
	
	gotoxy(75,21);
	color(14);
	printf("制");
	gotoxy(75,22);
	color(14);
	printf("作：");
	gotoxy(79,22);
	color(3);
	printf("陈");
	gotoxy(79,23);
	printf("颂");
	gotoxy(79,24);
	printf("斌");
}

int ksyx()
{
	int i,j;
	float t;
	zb xy[6];
	yxzjm();
	
	srand(time(NULL));
	i=rand()%7;
	while(1)
	{
		xy[0].x=((rand()%(RIGHT/2-LIFT/2-2))+(LIFT+2)/2)*2;
		if(js(i,xy[0].x)==0)
			break;
		flag=0;
		switch(i)
		{
			case 0: xy[0].y=3;i=rand()%7;ts(i);fk0(xy);xc();ts(-1);
				break;
			case 1: xy[0].y=5;i=rand()%7;ts(i);fk1(xy);xc();ts(-1);
				break;
			case 2: xy[0].y=4;i=rand()%7;ts(i);fk2(xy);xc();ts(-1);
				break;
			case 3: xy[0].y=4;i=rand()%7;ts(i);fk3(xy);xc();ts(-1);
				break;
			case 4: xy[0].y=4;i=rand()%7;ts(i);fk4(xy);xc();ts(-1);
				break;
			case 5: xy[0].y=4;i=rand()%7;ts(i);fk5(xy);xc();ts(-1);
				break;
			case 6: xy[0].y=4;i=rand()%7;ts(i);fk6(xy);xc();ts(-1);
				break;
		}
	}
}

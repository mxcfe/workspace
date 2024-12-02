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

int fklx(zb xy[])							
{
	switch(xy[5].x)
	{
		case 0:fk0(xy);break; 
		case 1:fk1(xy);break; 
		case 2:fk2(xy);break; 
		case 3:fk3(xy);break; 
		case 4:fk4(xy);break; 
		case 5:fk5(xy);break; 
		case 6:fk6(xy);break; 
	}
}

int fk(zb xy[],int xdwz[])
{
	int i;
	color(xy[5].y); 
	xy[1].x=xy[0].x+xdwz[0];
	xy[1].y=xy[0].y+xdwz[1];
	xy[2].x=xy[0].x+xdwz[2];
	xy[2].y=xy[0].y+xdwz[3];
	xy[3].x=xy[0].x+xdwz[4];
	xy[3].y=xy[0].y+xdwz[5];
	if(pd(xy)==0&&zyy(xy)==0)
	{
		flag--;
		fklx(xy);
	}
	for(i=0;i<4;i++)
	{
		gotoxy(xy[i].x,xy[i].y);
		printf("¡ö");
	}
	while(xl(xy)==1)
	{
		Sleep(TIME);
	}
	wzjl(xy);

}

int fk0(zb xy[])
{
	int xdwz[6]={2,0,0,1,2,1};
	xy[5].x=0;
	xy[5].y=10;
	fk(xy,xdwz);
}

int fk1(zb xy[])
{
	int xdwz[2][6]={{0,-2,0,-1,0,1},{-4,0,-2,0,2,0}};
	xy[5].x=1;
	xy[5].y=13;
	fk(xy,xdwz[flag%2]);
}

int fk2(zb xy[])
{
	int xdwz[2][6]={{-2,-1,0,-1,2,0},{2,-1,2,0,0,1}};
	xy[5].x=2;
	xy[5].y=6;
	fk(xy,xdwz[flag%2]);
}

int fk3(zb xy[])
{
	int xdwz[2][6]={{2,-1,0,-1,-2,0},{-2,-1,-2,0,0,1}};
	xy[5].x=3;
	xy[5].y=6;
	fk(xy,xdwz[flag%2]);
}

int fk4(zb xy[])
{
	int xdwz[4][6]={{-2,0,0,-1,2,0},{0,-1,2,0,0,1},{2,0,0,1,-2,0},{0,1,-2,0,0,-1}};
	xy[5].x=4;
	xy[5].y=3;
	fk(xy,xdwz[flag%4]);
}

int fk5(zb xy[])
{
	int xdwz[4][6]={{-2,-1,0,-1,0,1},{2,-1,2,0,-2,0},{2,1,0,1,0,-1},{-2,1,-2,0,2,0}};
	xy[5].x=5;
	xy[5].y=14;
	fk(xy,xdwz[flag%4]);
}

int fk6(zb xy[])
{
	int xdwz[4][6]={{2,-1,0,-1,0,1},{2,1,2,0,-2,0},{-2,1,0,1,0,-1},{-2,-1,-2,0,2,0}};
	xy[5].x=6;
	xy[5].y=14;
	fk(xy,xdwz[flag%4]);
}

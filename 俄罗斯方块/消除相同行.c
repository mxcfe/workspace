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

int xc()                                    
{
	int x,y,n,cnt=0;
	for(y=DOWN-1;y>UP;y--)
	{
		n=y;
		for(x=LIFT+2;x<RIGHT;x+=2)
			if(a[x][y]==0)
			break;
		if(x==RIGHT)
		{
			for(y=DOWN-1;y>UP;y--)
			{
				for(x=LIFT+2;x<RIGHT;x+=2)
				{
						gotoxy(x,y);
						printf("  ");
				} 
			}
			for(y=n;y>UP+1;y--)
			{
				for(x=LIFT+2;x<RIGHT;x+=2)
				{
					a[x][y]=a[x][y-1];
					b[x][y]=b[x][y-1];
				}
			} 
			for(x=LIFT+2;x<RIGHT;x+=2)
			{
				a[x][UP+1]=0;
				b[x][UP+1]=0;
			}
			
			for(y=DOWN-1;y>UP;y--)
			{
				for(x=LIFT+2;x<RIGHT;x+=2)
					{
						if(a[x][y]==1)
						{	
							gotoxy(x,y);
							color(b[x][y]);
							printf("■");
						}
					}
			}
			cnt++;
			y=n+1;
		}
	}
	fs+=cnt*cnt*10;
	TIME-=cnt*50;
	if(TIME<50)
		TIME=50;
	gotoxy(55,5);
	color(14);
	printf("目前得分：%d",fs);
	gotoxy(55,7);
	printf("目前下落速度：%dms   ",TIME);
}


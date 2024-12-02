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

int zyy(zb xy[])
{
	int i;
	for(i=2;i<6;i+=2)
	{
			xy[0].x+=i;
			xy[1].x+=i;
			xy[2].x+=i;
			xy[3].x+=i;
			if(pd(xy)==1)
			{
				wzbh(xy,0,0);
				return 1;
			}
			else
			{
			xy[0].x-=i;
			xy[1].x-=i;
			xy[2].x-=i;
			xy[3].x-=i;				
			}
			
			xy[0].x-=i;
			xy[1].x-=i;
			xy[2].x-=i;
			xy[3].x-=i;				
			if(pd(xy)==1)
			{
				wzbh(xy,0,0);
				return 1;
			}
			else
			{
			xy[0].x+=i;
			xy[1].x+=i;
			xy[2].x+=i;
			xy[3].x+=i;
			}
		}
	return 0;
}


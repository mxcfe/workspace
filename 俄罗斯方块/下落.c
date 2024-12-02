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

int xl(zb xy[])
{
	color(xy[5].y); 
	cz(xy);
	xy[0].y++;
	xy[1].y++;
	xy[2].y++;
	xy[3].y++;
	if(pd(xy)==1)
	{
		wzbh(xy,0,-1);
	}
	else
	{
		xy[0].y--;
		xy[1].y--;
		xy[2].y--;
		xy[3].y--;
		return 0;
	}
	return 1;
}

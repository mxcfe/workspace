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

int pd(zb xy[])				
{
	int i;
	for(i=0;i<4;i++)
	{
		if(a[xy[i].x][xy[i].y]==1)
			return 0;
	}
	return 1;
}

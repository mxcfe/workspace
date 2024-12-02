#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <time.h>
#define UP 2
#define DOWN 28
#define LIFT 14
#define RIGHT 48

extern int flag,fs,zgf,TIME,a[100][30],b[100][30];

int csh()
{
	int x,y;
	fs=0;
	TIME=1000;
	for(x=0;x<100;x++)
			for(y=0;y<30;y++)
			{
				if(x<=LIFT||x>=RIGHT||y<=UP||y>=DOWN)
					a[x][y]=1;
				else 
					a[x][y]=0;
			}
}

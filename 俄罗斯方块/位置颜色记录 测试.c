#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <time.h>
#define UP 2
#define DOWN 28
#define LIFT 14
#define RIGHT 48

extern int flag,fs,zgf,TIME,CS,a[100][30],b[100][30];

typedef struct
{
	int x;
	int y;
}zb;

int wzjl(zb xy[])					
{
	int i,x,y;
	for(i=0;i<4;i++)
	{
		a[xy[i].x][xy[i].y]=1;
		
		b[xy[i].x][xy[i].y]=xy[5].y;		
	}
	if(CS==1)
	{
		gotoxy(0,29);
		color(7);
		for(y=0;y<30;y++)
		{
			for(x=0;x<100;x++)
			{
				if(x>=LIFT&&x<=RIGHT&&y>=UP&&y<=DOWN)
				{
					gotoxy(68+x,y);
					if(x%2==0)
						printf("%d",a[x][y]);
					else
						printf(" ");
					gotoxy(0,0);
				}
			}
			printf("\n");
		}
	 } 

}


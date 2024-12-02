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

int wzbh(zb xy[],int a,int b)			
{
	int i;
	for(i=0;i<4;i++)
			{
				gotoxy(xy[i].x+a,xy[i].y+b);
				printf("  ");
			}
			for(i=0;i<4;i++)
			{
				gotoxy(xy[i].x,xy[i].y);
				printf("■");
			}
}


int cz(zb xy[])				
{
	int i=0;
	char ch;
	while(kbhit())
	{
        ch=getch();
            switch(ch)
            {
            case 72:
					flag++;
					for(i=0;i<4;i++)
					{
						gotoxy(xy[i].x,xy[i].y);
						printf("  ");
					}
					fklx(xy);
					break;
            case 80:
					while(1)
					{
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
					}
					break;
            case 75:
                	xy[0].x-=2;
					xy[1].x-=2;
					xy[2].x-=2;
					xy[3].x-=2;				
					if(pd(xy)==1)
					{
						wzbh(xy,2,0);
					}
					else
					{
						xy[0].x+=2;
						xy[1].x+=2;
						xy[2].x+=2;
						xy[3].x+=2;
					} 
					break;    
            case 77:
               		xy[0].x+=2;
					xy[1].x+=2;
					xy[2].x+=2;
					xy[3].x+=2;
					if(pd(xy)==1)
					{
						wzbh(xy,-2,0);
					}
					else
					{
						xy[0].x-=2;
						xy[1].x-=2;
						xy[2].x-=2;
						xy[3].x-=2;				
					}
					break;
            case 32:
                	color(13); 
					gotoxy(55,24);
					printf("游戏已暂停") ;
					gotoxy(55,25);
					system("pause");
					gotoxy(55,24);
					printf("游戏已开始");
					gotoxy(55,25);
					printf("                    ");
					color(xy[5].y); 
					break;
            case 27:
                   	gotoxy(55,24);
					color(13);
					printf("游戏已退出");
                   	gotoxy(0,28);
					exit(0);
       		}
		} 
}


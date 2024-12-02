#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <time.h>
#define UP 2
#define DOWN 28
#define LIFT 14
#define RIGHT 48

int a[100][30];
int b[100][30]; 
int flag,fs=0,zgf;
int TIME=1000; 
int CS=0; 
void gotoxy(int x,int y)
{
	COORD pos;
	pos.X=x;
	pos.Y=y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),pos);
}

int color(int c)
{
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c);
	return 0;
}

int CSHS()
{
	printf("\n是否开启测试模式[1.开启 0.关闭]：[ ]\b\b");
	scanf("%d",&CS);
 
}

int main()
{

	int x,y,i,j;
	
	i=zjm();
	while(1)
	{	
		csh();
		switch(i) 
		{
			case 1: ksyx();
					fen();
					if(jsjm()==2)
						i=zjm();
					break;
			case 2: fun2();
					i=zjm();
					break;
			case 3: if(fun3(fen())==2)
						guiling();
					system("cls");
					i=zjm();
					break;
			case 4: exit(0);
			case 5: CSHS();
			default:i=zjm();
		}
	}
	 
	return 0;
} 

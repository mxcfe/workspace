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

void guiling()
{
	FILE *fp;
	char c;
	int i;
	gotoxy(15,17); 
	color(13);
	printf("您的数据将清零[Y/N]:[ ]\b\b");
	scanf("%c",&c);
	scanf("%c",&c);
	if(c=='Y'||c=='y') 
	{
		fp=fopen("zgf.dat","wb+");
		zgf=0;
		fs=0;  
		fwrite(&zgf,sizeof(zgf),1,fp);
		fclose(fp);
		
				gotoxy(15,19); 
				printf("正在清零.   ");
				gotoxy(24,19); 
				for(i=0;i<3;i++)
				{
					Sleep(500);
					printf(".");
				 } 
				gotoxy(15,19); 
				printf("正在清零.   ");
				gotoxy(24,19); 
				for(i=0;i<3;i++)
				{
					Sleep(500);
					printf(".");
				 } 
				 
		gotoxy(15,19); 
		printf("数据已清零");
		system("pause");
	}
	else
	{ 
		gotoxy(15,18); 
		printf("数据未清零");
		system("pause");
	} 
}	

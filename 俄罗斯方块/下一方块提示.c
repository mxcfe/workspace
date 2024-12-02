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

int ts(int i)							
{
	switch(i)
	{
		case -1:
			gotoxy(60,13);
			printf("          "); 
			gotoxy(60,14);
			printf("          "); 
			gotoxy(60,15);
			printf("          ");
		 	gotoxy(60,16);
			printf("          "); 
			break;
		case 0:
			color(10);
			gotoxy(60,13);
			printf("¡ö¡ö"); 
			gotoxy(60,14);
			printf("¡ö¡ö"); 
			break;
		case 1:
			color(13);
			gotoxy(60,13);
			printf("¡ö"); 
			gotoxy(60,14);
			printf("¡ö"); 
			gotoxy(60,15);
			printf("¡ö");
		 	gotoxy(60,16);
			printf("¡ö"); 
			break;
		case 2:
			color(6);
			gotoxy(60,13);
			printf("¡ö¡ö"); 
			gotoxy(62,14);
			printf("¡ö¡ö"); 
			break;
		case 3:
			color(6);
			gotoxy(62,13);
			printf("¡ö¡ö"); 
			gotoxy(60,14);
			printf("¡ö¡ö"); 
			break;
		case 4:
			color(3);
			gotoxy(62,13);
			printf("¡ö"); 
			gotoxy(60,14);
			printf("¡ö¡ö¡ö"); 
			break;
		case 5:
			color(14);
			gotoxy(60,13);
			printf("¡ö¡ö"); 
			gotoxy(62,14);
			printf("¡ö"); 
			gotoxy(62,15);
			printf("¡ö"); 
			break;
		case 6:
			color(14);
			gotoxy(60,13);
			printf("¡ö¡ö"); 
			gotoxy(60,14);
			printf("¡ö"); 
			gotoxy(60,15);
			printf("¡ö"); 
			break;

	}
 } 
	

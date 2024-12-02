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

int fen()
{
	FILE *fp;
	if((fp=fopen("zgf.dat","rb"))==NULL)
		{
			fp=fopen("zgf.dat","wb+");
			zgf=0;
			fwrite(&zgf,sizeof(zgf),1,fp);
			fclose(fp);
		}
	else
		fread(&zgf,sizeof(zgf),1,fp);
		fclose(fp);
	if(fs>zgf) 
		zgf=fs;
	fp=fopen("zgf.dat","wb+");
	fwrite(&zgf,sizeof(zgf),1,fp);
	fclose(fp);
	return zgf;
}


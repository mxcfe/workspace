#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <time.h>
#define UP 2
#define DOWN 28
#define LIFT 14
#define RIGHT 48 

int dh(int *flag)
{
	char ch;
	while(kbhit())
        ch=getch();
        switch(ch)
        {
        	case 75:*flag=1;break;
        	case 77:*flag=2;break;
        	case 27:*flag=3;break;
        	
		}
	return *flag;
}

void fun2()
{
	int i,j=-15,k,flag=1;

	do{	
		while(dh(&flag)==2)
		{
			dh2(&flag);
		}
		
		if(flag==1)
		{
   			system("cls");
		}
		
		while(dh(&flag)==1)
		{
			dh1(&flag);	
		}
		if(flag==2)
		{
   			system("cls");
   			
		}
		
		if(dh(&flag)==3)break;
		
	}while(1);

}


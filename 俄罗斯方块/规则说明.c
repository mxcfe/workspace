#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <time.h>
#define UP 2
#define DOWN 28
#define LIFT 14
#define RIGHT 48

void dh1(int *flag)
{
	int i,j=-18,k;
	while(dh(flag)==1)
	{
		color(14);
		for(i=0,k=0;i<15&&dh(flag)==1;i++,k++)
		{
			if(i<=10)
			{
				gotoxy(63+i+j,13); 
				printf(":");
				k--;
			}
			else
			{
				gotoxy(61+i+j+k,13+(i-10)-4); 
				printf("::::");
				gotoxy(61+i+j+k,13-(i-10)+4); 
				printf("::::");
			}
		}
		
		for(k=0;k<9;k++)
		{
			gotoxy(90,10+k); 
			printf("                               ");				
		}
		for(k=0;k<9;k++)
		{
			gotoxy(54,10+k); 
			printf("      ::       ");				
		}
		gotoxy(0,0);
			color(11);
			printf("\n\n\n");
			printf("\t\t------------------规则说明--------------------\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    1、游戏空间                           ::\n");
			printf("\t\t::      玩家在一个16x24范围的空间内，       ::\n");
			printf("\t\t::      进行游戏                            ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    2、游戏包含多种图形                   ::\n");
			printf("\t\t::      正方形、Z型（左向，右向）、T        ::\n");
			printf("\t\t::      型 、L型（左向，右向）、长条        ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    3、下落规则                           ::\n");
			printf("\t\t::      每次系统随机从屏幕上方正中下        ::\n");
			printf("\t\t::      落一个图形，系统会提示              ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    4、消除规则                           ::\n");
			printf("\t\t::      当玩家控制的下落图形填满横向        ::\n");
			printf("\t\t::      一行所有空格时，本行自动消除        ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    5、计分规则                           ::\n");
			printf("\t\t::      一次消除n行得n*n分                  ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    6、结束规则                           ::\n");
			printf("\t\t::      当正中图形无法下落时，游戏结束      ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t----------------------------------------------\n");
			gotoxy(70,19); 
			color(15);
		printf("按“→”键转下一页");
		gotoxy(70,20); 
		printf("按“Esc”键返回主菜单");
		gotoxy(69,18); 
		Sleep(60);
		gotoxy(69,18); 
		
		for(i=0,k=0;i<16&&dh(flag)==1;i++,k++)
		{
			if(i<=10)
			{
				gotoxy(63+i+j,13); 
				printf(" ");
				k--;
			}
			else
			{
				gotoxy(61+i+j+k,13+(i-10)-4); 
				printf("    ");
				gotoxy(61+i+j+k,13-(i-10)+4); 
				printf("    ");
			}
		}
		j++;
		if(j>25){printf("%d",61+i+j+k);
		j=-18;}
	}
}


#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <time.h>
#define UP 2
#define DOWN 28
#define LIFT 14
#define RIGHT 48

void dh2(int *flag)
{
	int i,j=-15,k;
	while(dh(flag)==2)
	{
		color(14);
		for(i=0,k=0;i<15&&dh(flag)==2;i++,k++)
		{
			
			if(i<=10)
			{
				gotoxy(46-i-j,13); 
				printf(":");
				k--;
			}
			else
			{
				gotoxy(46-i-j-k,13+(i-10)-4); 
				printf("::::");
				gotoxy(46-i-j-k,13-(i-10)+4); 
				printf("::::");
			}
		}
		
		for(k=0;k<9;k++)
		{
			gotoxy(40,10+k); 
			printf("        ");				
		}
		for(k=0;k<9;k++)
		{
		gotoxy(0,10+k);
		printf("                    ");
		}
			gotoxy(0,0);
			printf("\n\n\n");
			color(11);
			printf("\t\t\t\t\t\t------------------按键说明--------------------\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    玩家使用键盘控制当前下落图形          ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    1、←→图形的移动                     ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    2、↓下落到最低                       ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    3、↑顺时针90度旋转图形               ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    4、当图形下落至游戏空间底部           ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::       或接触其他触底图形时，下           ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::       落停止，玩家无法继续操控           ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::       此图形                             ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    5、游戏中按Esc键直接退出程序          ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    6、空格键暂停游戏                     ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t----------------------------------------------\n");
			gotoxy(20,19); 
			color(15);
			printf("按“←”键转上一页");
			gotoxy(20,20); 
			printf("按“Esc”键返回主菜单");
		gotoxy(0,17); 

		Sleep(60);
		gotoxy(0,17); 
		
		for(i=0,k=0;i<16&&dh(flag)==2;i++,k++)
		{
			if(i<=10)
			{
				gotoxy(46-i-j,13); 
				printf(" ");
				k--;
			}
			else
			{
				gotoxy(46-i-j-k,13+(i-10)-4); 
				printf("    ");
				gotoxy(46-i-j-k,13-(i-10)+4); 
				printf("    ");
			}
		}
		j++;
		if(j>25)j=-15;
	}
}


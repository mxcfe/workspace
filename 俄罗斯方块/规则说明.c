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
			printf("\t\t------------------����˵��--------------------\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    1����Ϸ�ռ�                           ::\n");
			printf("\t\t::      �����һ��16x24��Χ�Ŀռ��ڣ�       ::\n");
			printf("\t\t::      ������Ϸ                            ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    2����Ϸ��������ͼ��                   ::\n");
			printf("\t\t::      �����Ρ�Z�ͣ��������򣩡�T        ::\n");
			printf("\t\t::      �� ��L�ͣ��������򣩡�����        ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    3���������                           ::\n");
			printf("\t\t::      ÿ��ϵͳ�������Ļ�Ϸ�������        ::\n");
			printf("\t\t::      ��һ��ͼ�Σ�ϵͳ����ʾ              ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    4����������                           ::\n");
			printf("\t\t::      ����ҿ��Ƶ�����ͼ����������        ::\n");
			printf("\t\t::      һ�����пո�ʱ�������Զ�����        ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    5���Ʒֹ���                           ::\n");
			printf("\t\t::      һ������n�е�n*n��                  ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t::    6����������                           ::\n");
			printf("\t\t::      ������ͼ���޷�����ʱ����Ϸ����      ::\n");
			printf("\t\t::                                          ::\n");
			printf("\t\t----------------------------------------------\n");
			gotoxy(70,19); 
			color(15);
		printf("����������ת��һҳ");
		gotoxy(70,20); 
		printf("����Esc�����������˵�");
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


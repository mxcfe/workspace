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
			printf("\t\t\t\t\t\t------------------����˵��--------------------\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    ���ʹ�ü��̿��Ƶ�ǰ����ͼ��          ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    1������ͼ�ε��ƶ�                     ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    2�������䵽���                       ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    3����˳ʱ��90����תͼ��               ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    4����ͼ����������Ϸ�ռ�ײ�           ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::       ��Ӵ���������ͼ��ʱ����           ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::       ��ֹͣ������޷������ٿ�           ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::       ��ͼ��                             ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    5����Ϸ�а�Esc��ֱ���˳�����          ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::    6���ո����ͣ��Ϸ                     ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t::                                          ::\n");
			printf("\t\t\t\t\t\t----------------------------------------------\n");
			gotoxy(20,19); 
			color(15);
			printf("����������ת��һҳ");
			gotoxy(20,20); 
			printf("����Esc�����������˵�");
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


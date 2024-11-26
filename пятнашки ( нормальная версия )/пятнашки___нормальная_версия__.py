# -*- coding: cp1251 -*-
import random
import numpy as np
from prettytable import PrettyTable

def fill_pole(pole):
#��������� ���� �� ������ 
    used_x = [] #�������������� �����
    for i in range (4): #�������� �� ��������
        for j in range(4): #�������� �� ������
            x = random.randint(0,15) #������ �� 0 �� 15 (����� � ������� ���� �����������?)
            while x in used_x: #������� �� ������ �����
                x = random.randint(0,15)
            used_x.append(x) #���������� ����� � ������ ��������������
            pole[i].append(x) #��������� ����� � ���� 
            if pole[i][j] == 0:
                pole[i][j] = ' '
    print(pole)
    return pole


def print_pole(pole):
#����� ����
    used_num = []
    x = PrettyTable()
    x.field_names = ['���','���','��','ALPHA']
    for j in range(4): #�������� �� �������
        x.add_row([pole [0][j],pole[1][j],pole[2][j],pole[3][j]])
               
    print(x)


def mexanika(pole, win_pole):
    while pole != win_pole:
        for i in range(4):
            for j in range(4):
                if pole[i][j] == ' ':
                  swap_0_x = i
                  swap_0_y = j

        swap_1 = input('������� ������, ������� ������ ����������� ')
        while swap_1 not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']:
            swap_1 = input('��� ������ �� ��������, �������� ������ ')
        swap_1 = int(swap_1)
        
        ok = True
        while ok == True:
            for i in range(4):
                for j in range(4):
                    if pole[i][j] == swap_1:
                        swap_1_x = i 
                        swap_1_y = j 
                        if ((swap_1_x == swap_0_x - 1) and (swap_1_y == swap_0_y)) or ((swap_1_x == swap_0_x + 1) and (swap_1_y == swap_0_y)) or ((swap_1_x == swap_0_x) and (swap_1_y == swap_0_y - 1)) or ((swap_1_x == swap_0_x) and (swap_1_y == swap_0_y + 1)):
                            ok = False 
                        else: 
                            swap_1 = input('������� ������ ������, ������� ������ ����������� ')
                            while swap_1 not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']:
                                swap_1 = input('��� ������ �� ��������, �������� ������� ')
                            swap_1 = int(swap_1)
        a = swap_1 
        pole[swap_1_x][swap_1_y] = ' '
        pole[swap_0_x][swap_0_y] = a
        print_pole(pole)
        

def main():
    win_pole = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,' ']] #�������� ����
    pole = [[],[],[],[]] #���� (��������� ������)
    pole = fill_pole(pole)
    print_pole(pole)
    mexanika(pole, win_pole)
main()
import random
import numpy as np
from prettytable import PrettyTable

def fill_pole(pole):
    
#заполняем поле на рандом 
    used_x = [] #использованные числа
    for i in range (4): #проходка по столбцам
        for j in range(4): #проходка по строке
            x = random.randint(0,15) #рандом от 0 до 15 
            while x in used_x: #провека на повтор числа
                x = random.randint(0,15)
            used_x.append(x) #добавление числа в список использованных
            pole[i].append(x) #добавляем число в поле 
            if pole[i][j] == 0:
                pole[i][j] = ' '
    print(pole)
    return pole


def print_pole(pole):
#вывод поля
    used_num = []
    x = PrettyTable()
    x.field_names = ['ПЯТ','НАШ','КИ','ALPHA']   # ХОЧУ НОРМАЛЬНУЮ ТАБЛИЦУ!!!!!!!!!!!!!!!!!!!
    for j in range(4): #проходка по строкам
        x.add_row([pole [0][j],pole[1][j],pole[2][j],pole[3][j]])
               
    print(x)


def mexanika(pole, win_pole):
    while pole != win_pole:
        for i in range(4):
            for j in range(4):
                if pole[i][j] == ' ':
                  swap_0_x = i
                  swap_0_y = j

        swap_1 = input('Введите клетку, которую хотите переместить: ')
        while swap_1 not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']:
            swap_1 = input('Эта клетка не рядом с пустой ячейкой, введите другую: ')
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
                            swap_1 = input('Ââåäèòå äðóãóþ êëåòêó, êîòîðóþ õîòèòå ïåðåìåñòèòü ')
                            while swap_1 not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']:
                                swap_1 = input('Ýòà êëåòêà íå äîñòóïíà, âûáåðèòå äðóãóþõ ')
                            swap_1 = int(swap_1)
        a = swap_1 
        pole[swap_1_x][swap_1_y] = ' '
        pole[swap_0_x][swap_0_y] = a
        print_pole(pole)
        

def main():
    win_pole = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,' ']]  #победное поле
    pole = [[],[],[],[]] #поле (двумерный массив)
    pole = fill_pole(pole)
    print_pole(pole)
    mexanika(pole, win_pole)
main()

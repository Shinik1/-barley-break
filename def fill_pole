import random

def fill_pole(pole):
#заполняем поле на рандом 
    used_x = [] #использованные числа
    for i in range (4): #проходка по столбцам
        for j in range(4): #проходка по строке
            x = random.randint(0,15) #рандом от 0 до 15 (зачем я написал этот комментарий?)
            while x in used_x: #провека на повтор числа
                x = random.randint(0,15)
            used_x.append(x) #добавление числа в список использованных
            pole[i].append(x) #добавляем число в поле 
            if pole[i][j] == 0:
                pole[i][j] = ' '
    print(pole)
    return pole

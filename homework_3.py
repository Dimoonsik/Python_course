a = int(input('Введи первое число: '))
b = int(input('Введи второе число: '))
c = int(input('Введи третье число: '))
nol = a == 0 or b == 0 or c == 0 or 'Нет нулевых значений!!!'
nenol = a or b or c or 'Введены все нули!'
print(nol)
print(nenol)
if a > b + c:           # я так понял нужно было посчитать, а не выводить 'a-b-c' 
    print(a - b - c) 
if a < b + c:
    print(b + c - a)
if a > 50 and (b > a or c > a):
    print('Вася')
if a > 5 or b == c == 7:   # можно было a > 5 or (b == 7 and c == 7)
    print('Петя')



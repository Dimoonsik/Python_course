import math
x = 0
y = 0
shag = 0
while True:
    shag = input('введите ход (u/d/l/r число): ')
    if shag == '':
        break
    else:
        shag.split(' ')
        if shag[0] == 'u':
            y = y + int(shag[2]) 
        elif shag[0] == 'd':
            y = y - int(shag[2])
        elif shag[0] == 'l':
            x = x - int(shag[2])
        elif shag[0] == 'r':
            x = x + int(shag[2]) 
x_raznica = x - 0
y_raznica = y - 0
c_kvardat = x_raznica ** 2 + y_raznica ** 2
c = math.sqrt(c_kvardat)
print(c)

import time
import datetime
import os
s = '\u2B1B'
w = '\u2B1C'
zero = [
    w * 7,
    w * 2 + s * 3 + w * 2,
    w * 2 + s * 3 + w * 2,
    w * 2 + s * 3 + w * 2,
    w * 2 + s * 3 + w * 2,
    w * 7
]

one = [
    w * 4 + s * 3,
    s * 3 + w + s * 3,
    s * 3 + w + s * 3,
    s * 3 + w + s * 3,
    s * 3 + w + s * 3,
    w * 7
]

two = [
    w * 7,
    w + s * 3 + w * 3,
    s * 3 + w * 3 + s,
    s * 2 + w * 3 + s * 2,
    s * 1 + w * 3 + s * 3,
    w * 7
]

three = [
    w * 7,
    w + s * 3 + w * 3,
    s * 4 + w + s * 2,
    s * 5 + w * 2,
    w + s * 4 + w * 2,
    w * 5 + s * 2  
]

four = [
    w * 2 + s * 3 + w * 2,
    w * 2 + s * 3 + w * 2,
    w * 7,
    s * 5 + w * 2,
    s * 5 + w * 2,
    s * 5 + w * 2
]

five = [
    w * 7,
    w * 2 + s * 5,
    w * 7,
    s * 4 + w * 3,
    w * 2 + s * 2 + w * 3,
    w * 5 + s * 2
]

six = [
    s * 1 + w * 6,
    w * 2 + s * 5,
    w * 7,
    w * 2 + s * 2 + w * 3,
    w * 2 + s * 2 + w * 3,
    w * 6 + s * 1
]

seven = [
    w * 7,
    s * 5 + w * 2,
    s * 4 + w * 2 + s,
    s * 3 + w * 2 + s * 2,
    s * 2 + w * 2 + s * 3,
    s * 1 + w * 2 + s * 4
]

eight = [
    w * 7,
    w * 2 + s * 3 + w * 2,
    w * 7,
    w * 7,
    w * 2 + s * 3 + w * 2,
    w * 7
]

nine = [
    w * 7,
    w * 2 + s * 3 + w * 2,
    w * 7,
    s * 3 + w * 2 + s * 2,
    s * 2 + w * 2 + s * 3,
    s * 1 + w * 2 + s * 4
]

double_dot = [
    s,
    w,
    s,
    s,
    w,
    s
]

no_dot = [
    s,
    s,
    s,
    s,
    s,
    s
]
total = 2

while True:
    cdt = datetime.datetime.now()
    ct_1 = cdt.strftime("%H:%M:%S")
    clock = []
    if total % 2 == 0:
        for i in ct_1:
            if i == '0':
                clock.append(zero)
            elif i == '1':
                clock.append(one)
            elif i == '2':
                clock.append(two)
            elif i == '3':
                clock.append(three)    
            elif i == '4':
                clock.append(four)
            elif i == '5':
                clock.append(five)
            elif i == '6':
                clock.append(six)
            elif i == '7':
                clock.append(seven)
            elif i == '8':
                clock.append(eight)
            elif i == '9':
                clock.append(nine)
            elif i == ':':
                clock.append(double_dot)   
        print(clock[0][0] + ' ' + clock[1][0] + ' ' + clock[2][0] + ' ' + clock[3][0] + ' ' + clock[4][0] + ' ' + clock[5][0] + ' ' + clock[6][0] + ' ' + clock[7][0])
        print(clock[0][1] + ' ' + clock[1][1] + ' ' + clock[2][1] + ' ' + clock[3][1] + ' ' + clock[4][1] + ' ' + clock[5][1] + ' ' + clock[6][1] + ' ' + clock[7][1])
        print(clock[0][2] + ' ' + clock[1][2] + ' ' + clock[2][2] + ' ' + clock[3][2] + ' ' + clock[4][2] + ' ' + clock[5][2] + ' ' + clock[6][2] + ' ' + clock[7][2])
        print(clock[0][3] + ' ' + clock[1][3] + ' ' + clock[2][3] + ' ' + clock[3][3] + ' ' + clock[4][3] + ' ' + clock[5][3] + ' ' + clock[6][3] + ' ' + clock[7][3])
        print(clock[0][4] + ' ' + clock[1][4] + ' ' + clock[2][4] + ' ' + clock[3][4] + ' ' + clock[4][4] + ' ' + clock[5][4] + ' ' + clock[6][4] + ' ' + clock[7][4])
        print(clock[0][5] + ' ' + clock[1][5] + ' ' + clock[2][5] + ' ' + clock[3][5] + ' ' + clock[4][5] + ' ' + clock[5][5] + ' ' + clock[6][5] + ' ' + clock[7][5])
        time.sleep(0.2)
        total += 1
        clear = lambda: os.system('cls')
        clear()
    elif total % 2 != 0:
        for i in ct_1:
            if i == '0':
                clock.append(zero)
            elif i == '1':
                clock.append(one)
            elif i == '2':
                clock.append(two)
            elif i == '3':
                clock.append(three)    
            elif i == '4':
                clock.append(four)
            elif i == '5':
                clock.append(five)
            elif i == '6':
                clock.append(six)
            elif i == '7':
                clock.append(seven)
            elif i == '8':
                clock.append(eight)
            elif i == '9':
                clock.append(nine)
            elif i == ':':
                clock.append(no_dot)   
        print(clock[0][0] + ' ' + clock[1][0] + ' ' + clock[2][0] + ' ' + clock[3][0] + ' ' + clock[4][0] + ' ' + clock[5][0] + ' ' + clock[6][0] + ' ' + clock[7][0])
        print(clock[0][1] + ' ' + clock[1][1] + ' ' + clock[2][1] + ' ' + clock[3][1] + ' ' + clock[4][1] + ' ' + clock[5][1] + ' ' + clock[6][1] + ' ' + clock[7][1])
        print(clock[0][2] + ' ' + clock[1][2] + ' ' + clock[2][2] + ' ' + clock[3][2] + ' ' + clock[4][2] + ' ' + clock[5][2] + ' ' + clock[6][2] + ' ' + clock[7][2])
        print(clock[0][3] + ' ' + clock[1][3] + ' ' + clock[2][3] + ' ' + clock[3][3] + ' ' + clock[4][3] + ' ' + clock[5][3] + ' ' + clock[6][3] + ' ' + clock[7][3])
        print(clock[0][4] + ' ' + clock[1][4] + ' ' + clock[2][4] + ' ' + clock[3][4] + ' ' + clock[4][4] + ' ' + clock[5][4] + ' ' + clock[6][4] + ' ' + clock[7][4])
        print(clock[0][5] + ' ' + clock[1][5] + ' ' + clock[2][5] + ' ' + clock[3][5] + ' ' + clock[4][5] + ' ' + clock[5][5] + ' ' + clock[6][5] + ' ' + clock[7][5])
        time.sleep(0.2)
        total += 1
        clear = lambda: os.system('cls')
        clear()   

    
    







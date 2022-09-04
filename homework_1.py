message = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"

simbols = str(len(message))
print('Шаг 1 - колличество символов - ' + simbols)

mirror = message[::-1]
print('Шаг 2 - развернуть строку - ' + mirror)

first_big_letters = message.title()
print('Шаг 3 - каждое слово с большой буквы - ' + first_big_letters)

all_big_letters = message.upper()
print('Шаг 4 - текст прописными буквами - ' + all_big_letters)

nd_count = message.count('нд')
am_count = message.count('ам')
o_count = message.count('о')
print(f'шаг 5 - число вхождений в строку: нд - {str(nd_count)}, ам - {str(am_count)}, о - {str(o_count)}')  #чуть-чуть грязновато было изначально, но тут вспомнилась f-строка :)

capi = message.capitalize()
print('Шаг 6 - текст строчными буквами - ' + capi)

new_message = message.replace('человека', 'питониста')
print('Шаг 6 - текст с заменой - ' + new_message)

predl_message = message.split('. ')
predl_1 = predl_message[0].split(' ')      
predl_1 = predl_1[::-1] 
predl_1 = ' '.join(predl_1) 
print(f'Шаг 7 - развернуть предложение (как в тз) - {predl_1}')

predl_2_message = message.split(' ')
predl_2_message = predl_2_message[::-1]
predl_2_message = ' '.join(predl_2_message)
print(f'Шаг 7 - развернуть предложение (всю строку) - {predl_2_message}')

print(f'Шаг 8 - исходная команда - {message}')
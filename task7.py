message = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"

predl_message = message.split('. ')
predl_1 = predl_message[0].split(' ')      
predl_1 = predl_1[::-1] # развернет
predl_1 = ' '.join(predl_1) # объеднит назад
print(predl_1)
print('hello world from vetka')


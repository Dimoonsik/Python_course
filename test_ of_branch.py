name = input('Введите ваш логин: ')

if name != 'админ' and name != 'Админ':
    print('Доступ запрещен')
else:
    def decorator(func):
    
        def wrapper_decorator(login):
            
            value = func(login)
            return value 
    
        return wrapper_decorator

    @decorator
    def summa_scheta(login):
        return f'{login}, у тебя овер много денег на счете!'

    rezult = summa_scheta(name)      
    print(rezult)

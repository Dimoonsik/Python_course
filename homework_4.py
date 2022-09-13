
name = input('Введите ваш логин: ')



def decorator(func):
    
    def wrapper_decorator(login):
        if login != 'админ' and login != 'Админ':
            return 'Доступ запрещен'
        value = func(login)
        return value 
    
    return wrapper_decorator

@decorator
def summa_scheta(login):
    return f'{login}, у тебя овер много денег на счете!'

rezult = summa_scheta(name)      # я часа 2 сидел и не мог понять почему у меня ничего не работает, видимо 
                            #я упустил на занятии что нужно было ещё присвоить например переменной a - свою функцию и вывести на печать (спасибо великий гугл)...АААААААААААААААА
print(rezult)
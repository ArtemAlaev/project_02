# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

# Решение:

a = int(input('Введите номер месяца: '))
if 13 > a > 0:
    if a == 1: print('Вы ввели январь. 31 день')
    elif a == 2: print('Вы ввели февраль. 28 дней')
    elif a == 3: print('Вы ввели март. 31 день') 
    elif a == 4: print('Вы ввели апрель. 30 дней')
    elif a == 5: print('Вы ввели май. 31 день')
    elif a == 6: print('Вы ввели июнь. 30 дней')
    elif a == 7: print('Вы ввели июль. 30 дней')    
    elif a == 8: print('Вы ввели август. 31 день')    
    elif a == 9: print('Вы ввели сентябрь. 30 дней')    
    elif a == 10: print('Вы ввели октябрь. 31 день')    
    elif a == 11: print('Вы ввели ноябрь. 30 дней')    
    elif a == 12: print('Вы ввели декабрь. 31 день')    
else: print('Такого месяца нет!')
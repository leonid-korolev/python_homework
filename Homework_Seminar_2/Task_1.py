# 1 - Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11
def input_verification():
    digit = 1
    while digit:
        try:
            n = float(input('Введите число: '))
            n = abs(float(n))
            str_n = str(n)
            str_n = str_n.replace('.','')
            lst_str = list(str_n)
            lst_num = map(int, lst_str)
            s = sum(lst_num)
            print(f'{n} -> {s}')
            digit = 0
            quit()
        except ValueError:
            print ('Это не число!')
    return s        
print(input_verification())

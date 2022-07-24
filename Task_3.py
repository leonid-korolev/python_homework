# Задача_3
# Задайте натуральное число N. Напишите 
# программу, которая составит
# список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

def get_number():
    while True:
        n = input('Введите натуральное число: ')
        try:
            n = int(n)
            if n <= 0:
                print('Это число не относится к натуральным')
            else:
                return n
        except ValueError:
            print('Некорректный ввод')
        
n = get_number()
print(f'N = {n}')

def simple_mult(k):
    if k == 1:
        print(f'при N = {k} -> [{k}]')
        return k
    else:
        get_list = []
        fin_get_list = []
        i = 2
        while i <= k:
            if (k % i) == 0:
                get_list.append(i)
                k = k / i
            else:
                i += 1
    for i in get_list:
        if i not in fin_get_list:
            fin_get_list.append(i)
    print(get_list)
    print(f'Список простых множителей при N = {n} -> {fin_get_list}')
    print()                
    return get_list,fin_get_list

simple_mult(n)        






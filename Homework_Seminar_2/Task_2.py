# 2 - Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

try:
    number = int(input('Введите число: '))
except ValueError:
    print ('Это не число!')
    print()
list_number = [1]
str_n = [1] 
f = 1
   
for i in range(1,number):
    f *= i+1
    list_number.append(f)
print(list_number) 
print()   

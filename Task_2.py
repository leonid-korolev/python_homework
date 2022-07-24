# Задача_2
# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
#  Посмотрели, что такое множество? Вот здесь его не используйте.

import random

def random_numbers():
    nums = []
    for i in range(0,7):
        nums.append(random.randint(0,10)-random.randint(0,3))
    return nums

sequence = random_numbers()
print(sequence)

def sort_sequence(n):
    nums_1 = []
    for i in n:
        if sequence.count(i)==1:
            nums_1.append(i)
    print(nums_1)        
    return nums_1
sort_sequence(sequence)
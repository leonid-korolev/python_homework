# Задача_1
# Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi,
# а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона
# или серию Чудновских.

# Пример:

# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

# Вычисление по формуле Лейбница:
# X = 4 - 4/3 + 4/5 - 4/7 +4/9 - ...

def pi():
    k = 1
    pi = 0
    for i in range(1000000):
        if i%2 == 0:
            pi+= 4/k
        else:
            pi-= 4/k
        k+=2
    print(pi)    
    return (str(pi)[:5])
print(pi())
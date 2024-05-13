a, b = map(int,input('Введите через пробел числа a и b: ').split())
c, d = map(int,input('Введите через пробел числа c и d: ').split())
if (a, b, c, d < 10) and a <= b and c <= d:
    print(' ', end='\t')
    for i in range(c, d + 1):
        print(i, end='\t')
    print('')
    for j in range(a, b + 1):
        print(j, end='\t')
        for i in range(c, d + 1):
            print(i * j, end='\t')
        print('')
else:
    print("Введенные числа не соответствуют условию задачи")

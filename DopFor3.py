num = int(input("Введите число n: "))
count = 1
for i in range(1, num+1):
    for j in range(i):
        print(count, end='\t')
        count += 1
    print()
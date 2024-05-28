
a = int(input('Введите значение от 3 до 20: '))
print(a)
rez =[]
b = rez



for b1 in range(1,21):
    if a > b1*2:
        rez.append(b1)
        for b2 in range(1, 21):
            if a % (b1 + b2) == 0 and b2 != b1 and b2 > b1 or b2 == a - b1:
                rez.append(b2)



print(b)
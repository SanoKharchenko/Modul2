def generate_password(b):
    password = ''
    for i in range(1,b):
        for j in range(i + 1, b + 1):
            if b % (i + j) == 0:
                password += str(i) + str(j)
    return password

for b in range(3, 21):
    password = generate_password(b)
    #print(generate_password(b))
    print(f'{b} - {password}')


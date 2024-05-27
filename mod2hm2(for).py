numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
no_primes = []
is_prime = True

for i in numbers:
    is_prime = True
    for j in range(2, i//2+1):
        if i % j == 0:
            is_prime = False
            no_primes.append(i)
            break
    if is_prime:
        primes.append(i)
primes.remove(1)
print('Primes: ', primes)
print('No primes: ', no_primes)
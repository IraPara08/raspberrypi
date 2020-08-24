
primeresponse = input('What is a prime number, A) Numbers that have more than 1 multiple, B) Numbers that have one pair of factors?')
print(primeresponse)
if primeresponse == 'A':
        print('You have picked the wrong answer')
elif primeresponse == 'B':
        print('You have picked the right answer')
print('Here is an example of prime numbers')
primes = [1, 2, 3, 5, 7,]
for prime in primes:
    print(prime)

primenumberinputresponse = input('Enter a number: ')
primenumberint = int(primenumberinputresponse)

for x = 1 to primenumberint:
    if (primenumberint % x == 0):
        if (primenumber <> x && x <> 1):
            print('Not a prime')
            break
        else:
            continue
    else:
        continue

print('Prime Number')

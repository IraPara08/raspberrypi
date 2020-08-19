primenumberinputresponse = input('Enter a number: ')
primenumberint = int(primenumberinputresponse)

prime = True
for x in range(1, primenumberint):
    print(x)
    if (primenumberint % x == 0):
        if (primenumberint != x and x != 1):
            #print('Not a prime')
            prime = False
            break
        else:
            continue
    else:
        continue

if prime:
    print('Prime')
else:
    print('Not Prime')

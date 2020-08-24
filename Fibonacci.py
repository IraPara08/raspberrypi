#get user input for number of fibonacci numbers to create
inputnumber = input("Enter the number of fibonacci numbers you would like to create.")

#convert the user input to an integer
number = int(inputnumber)

#print the integer number
print(number)

#initialize a fibonacci list with first 2 numbers in the fibonacci sequence
fibonacci = [1,1]

#loop for x number of items starting at 3 fibonacci number
for x in range(2, number):
        #add previous fibonacci number to the one previous to that
        #print(x)
        #print(x-1)
        #print(x-2)
        #print(fibonacci[x-1])
        #print(fibonacci[x-2])
        fibonacci.append(fibonacci[x-1] + fibonacci[x-2])
        #print(fibonacci[x])

#print fibonacci sequence
print(fibonacci)

    


#Asking the amount of fibonacci numbers to be printed
inputnumber = input("How many numbers should be printed from the fibonacci Sequence?")
#Converting to integer
number = int(inputnumber)
#Print integer
print(number)
#First two numbers in fibonacci list
fibonacci = [1,1]
#
for x in range(2, number):
#pattern
        fibonacci.append(fibonacci[x-1] + fibonacci[x-2])
#print sequence
print(fibonacci)

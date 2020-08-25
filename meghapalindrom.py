#Ask user for word
wordinput = input("Please Type In A Word: ")

#Define reverse palindrome
reverseword = ''

#For loop
for x in range(len(wordinput)-1, -1, -1):
    reverseword = reverseword + wordinput[x]

#Print reverse word
print(reverseword)

#Compare
if wordinput == reverseword:
    print("This is a palindrome!")
else:
    print("This is not a palindrome:(")

#TA-DA
print("Ta-Da !")


                  

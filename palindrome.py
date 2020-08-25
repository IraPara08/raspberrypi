#Ask user for a word
wordinput = input("Please Type In A Word: ")

#Defining Reverse Word
reverseword = ''

#Start Loop
for x in range(len(wordinput)-1, -1, -1):
    reverseword = reverseword + wordinput[x]
    #print(wordinput[x])
    #print(x)

print(reverseword)

#Compare if revese word is the same as input word
    
if wordinput == reverseword:
    print("This is a palindrome!")
else:
    print("This is not a palindrome:(")

#TA-DA
print("Ta-Da!!")


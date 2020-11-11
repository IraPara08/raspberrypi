import random
print("Welcome to Hangman!")
wordbank = {'animals' : 'tiger', 'food' : 'bread', 'clothes' : 'jeans'} 
category, word = random.choice(list(wordbank.items()))
print(str(len(word))+' letters long')
print('category: ' + str(category))
guessword = ['-','-','-','-','-']
for _ in range(len(word)):
    inputcharacter = input()
    if (word.find(inputcharacter) != -1 ): 
        guessword[word.find(inputcharacter)] = inputcharacter
        print(guessword)
    else:
        print("Oopsedoopsie! Try again.")
if (str(guessword).find('-') != -1 ):
    print("Too late! You are out of tries. Play Again!")
else:
    print("Yay!!!!!! You've done it!!!!")

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:58:17 2023

@author: Bradley Sheldon
"""

import random
# Generates the random 4 digit code
secret_code =[]
for i in range (0,4):
    n = random.randint(1,9)
    secret_code.append(str(n))
b="".join(secret_code)

# Displays start of the game
print("Begin Mystery Code Game!")
print("Possible numbers:")
# Rearanges 4 digit code and displays the possible guesses
a="".join(sorted(secret_code))
print(a)
i=0
d=0

# Determines whether user has used all their guesses 
while i<5:
# Takes the users guess   
    print("Enter your guess:")
    x=input()
    l=list(x)
# Determines whether guess is correct or not
# If it is "Winner!!" is displayed    
    if x==b:
        print("Winner!! You broke the code")
        break
# If input is incorrect +1 is added to count and feedback on guess is provided  
    else:
        d+=1
        c=0
        for j in range(len(secret_code)):
            if l[j]==secret_code[j]:
                c+=1
        print("You guessed ",c,"correctly")   
    i=i+1
# Once count reaches 5 user looses
if d==5:
    print("Looser!")
    print("The answer is:",b)
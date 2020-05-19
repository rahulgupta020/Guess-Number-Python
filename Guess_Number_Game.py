import random
g=random.randint(1,100)
# print(g)
num=int(input("Enter a number between 1 to 100 :- "))
while(g!='num'):
    if g<num:
        print("Guess is low")
        num=int(input("Enter a number between 1 to 100 :- "))
    elif g>num:
        print("Guess is greater")
        num=int(input("Enter a number between 1 to 100 :- "))
    else:
        print("You guessed it!!!")
        break


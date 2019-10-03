import random
'''First mini-game
Guess the number
using random module'''
print("Guess the number. Limit 0-20")
n=random.randint(0,20)
tries=1
print(n)
while True:
    x=input('Enter your guess: ')
    x=int(x)
    print('\n')
    if (x == 100):
        print("Do not give up so easily")
        print("Are you sure you want to quit?\n")
        ch = input()
        if (ch == 'y'):
            break
        if (ch == 'n'):
            continue
    if(x<n):
        print("Wrong Guess...Try something larger!")
        tries+=1
    if(x>n):
        print("Too big...Try something smaller")
        tries+=1
    if(x==n):
        print("That's correct...Well done!")
        print("You guessed the number in {} tries".format(tries))
        break
    if(x==100):
        print("Do not give up so easily")
        print("Are you sure you want to quit?\n")
        ch=input()
        if(ch==y):
            break
        if(ch==n):
            continue


print('WELCOME TO THIS TREASURE HUNT')
print('Your goal is to find the treasure')

print('you are at a crossroads, where do you want to go?')
choice1 = input('left or right? \n')

if choice1 == 'left':
    print('Sorry, you lost.')

if choice1 == "right":
    choice2 = input('swim or wait? \n')

    if choice2 == "swim":
        print('Sorry, you drowned')

    if choice2 == "wait":
        choice3 = input('Which Door? Blue, Green or Yellow? \n')

        if choice3 == "blue" :
            print('Sorry, you drowned')
        if choice3 == "green" :
            print('Sorry, you drowned')
        if choice3 == "yellow":
            print('HURRAY! YOU WIN!!!!!!')
        else:
            print(' You lost.')

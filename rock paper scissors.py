import random

exit=False
user_points=0
computer_points=0

while exit==False:
    options=['rock','paper','scissors']
    user_input=input('choose rock, paper, scissors or exit:')
    computer_input=random.choice(options)

    if user_input=='exit':
        print('game ended')
        print(user_points,computer_points)
        exit=True

    if user_input=='rock':
        if computer_input=='rock':
            print("it's a tie")
        elif computer_input=='scissors':
            print('user won')
            user_points+=1
        elif computer_input=='paper':
            print('ai won')
            computer_points+=1
            
    elif user_input=='paper':
        if computer_input=='paper':
            print("it's a tie")
        elif computer_input=='rock':
            print('user won')
            user_points+=1
        elif computer_input=='scissors':
            print('ai won')
            computer_points+=1
            
    elif user_input=='scissors':
        if computer_input=='scissors':
            print("it's a tie")
        elif computer_input=='paper':
            print('user won')
            user_points+=1
        elif computer_input=='rock':
            print('ai won')
            computer_points+=1

    elif user_input!='scissors' or user_input!='paper' or user_input!='rock':
        print('invalid')
            
            
    

#!/usr/bin/env python3
round = 0
while(True):
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input()
    my_answer = answer.lower()

    if (my_answer == 'brian'):
        print('Correct')
        break
    elif (my_answer == 'shrubbery'):
        print('You gave the super secret answer!')
        break
    elif (round == 3):
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry!  Try again')


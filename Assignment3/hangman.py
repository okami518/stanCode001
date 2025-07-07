"""
File: hangman.py
Name: Kang
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    answer = random_word()
    print(f"The word looks like: {'-'*len(answer)}")
    print(answer)
    hang_man(answer)


def hang_man(answer):
    wrong_times = 0
    my_word = '-'*len(answer)
    while N_TURNS-wrong_times > 0:
        print(f"You have {N_TURNS-wrong_times} wrong guesses left.")
        input_ch = str(input('Your guess: ')).upper()
        if input_ch.isalpha() and len(input_ch) == 1:
            update_word = ''
            if input_ch in answer:
                for i in range(len(my_word)):
                    if answer[i] == input_ch:
                        update_word += answer[i]
                    elif my_word[i].isalpha():
                        update_word += my_word[i]
                    else:
                        update_word += '-'
                my_word = update_word
                print('You are correct!')
                if my_word == answer:
                    break

            else:
                print(f"There is no {input_ch}'s in the word")
                wrong_times += 1
            print(f"The word looks like: {my_word}")
        else:
            print('illegal format')

    if N_TURNS == wrong_times:
        print("You are completely hung :(")
    else:
        print("You win!!!")

    print(f'The answer is: {answer}')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

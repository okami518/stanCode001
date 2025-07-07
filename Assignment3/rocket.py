"""
File: rocket.py
Name: Kang
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')

        for k in range(i+1):
            print('/', end='')

        for ii in range(i+1):
            print('\\', end='')

        for j in range(SIZE, 0, -1):
            print(' ', end='')

        print('')


def belt():
    print('+', end='')
    for i in range(SIZE*2):
        print('=', end='')
    print('+')


def upper():
    for i in range(SIZE):
        print('|', end='')
        for j in range(2-i):
            print('.', end='')
        for ii in range(i+1):
            print('/', end='')
            print('\\', end='')
        for jj in range(2-i):
            print('.', end='')
        print('|')


def lower():
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            print('.', end='')
        for ii in range(3-i):
            print('\\', end='')
            print('/', end='')
        for jj in range(i):
            print('.', end='')
        print('|')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()

"""
File: hailstone.py
Name: Kang
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    print(1.0 == 1)
    print('This program computes Hailstone sequences.')
    num = int(input('Enter a number: '))
    steps = 0
    while True:
        if num == 1:
            break

        elif num % 2 == 0:
            print(f"{num} is even, so I make half: {num//2}")
            num = num // 2
            steps += 1
        else:
            print(f"{num} is odd, so I make 3n+1: {3*num+1}")
            num = 3*num + 1
            steps += 1

    print(f"It took {steps} to reach 1")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()

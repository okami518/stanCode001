"""
File: extension4_narcissistic_checker.py
Name: Kang
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    print('Welcome to the narcissistic number checker!')
    while True:
        n = int(input('n: '))
        square = len(str(n))
        if n != EXIT:
            while True:
                total = 0
                for i in range(len(str(n))):
                    total += int(str(n)[i])**square
                if n == total:
                    print(f'{n} is a narcissistic number')
                    break

                else:
                    print(f'{n} is not a narcissistic number')
                    break

        else:
            break

    print('Have a good one!')


if __name__ == '__main__':
    main()

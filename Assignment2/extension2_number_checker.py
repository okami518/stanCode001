"""
File: extension2_number_checker.py
Name: Kang
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    print('Welcome to the number checker!')
    while True:
        n = int(input('n: '))
        divisor = []  # 用list收納所有除了自己外的的因數，也比較省記憶體
        total = 0
        if n == EXIT:
            break
        else:
            for i in range(1, n, 1):
                if n % i == 0:  # 尋找因數
                    divisor.append(i)
            for i in range(len(divisor)):
                total += divisor[i]

            if total == n:
                print(f"{n} is a perfect number")

            elif total > n:
                print(f"{n} is a abundant number")

            else:
                print(f"{n} is a deficient number")

    print('Have a good one!')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

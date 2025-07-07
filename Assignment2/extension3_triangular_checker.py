"""
File: extension3_triangular_checker.py
Name: Kang
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    print("Welcome to the triangular number checker!")

    while True:
        s = 0

        n = int(input('n: '))
        if n != EXIT:
            while True:
                form = int(s * (s + 1) // 2)  # Ｑ：為什麼form放在第25行不會刷新
                if n == form:
                    print(f"{n} is a triangular number ")
                    break
                elif n < form:
                    print(f"{n} is not a triangular number ")
                    break
                else:
                    s += 1

        else:
            print('Have a good one!')
            break


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

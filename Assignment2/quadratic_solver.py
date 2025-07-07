"""
File: quadratic_solver.py
Name: Kang
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	print(f"stanCode Quadratic Solver!")
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	discriminant(a, b, c)


def discriminant(a, b, c):
	disc = b**2-4*a*c

	if disc < 0:
		print("No real roots")
	elif disc == 0:
		f1 = math.sqrt(disc)
		x = (-b + f1) / (2 * a)
		print(f"One root: {x}")
	else:
		f1 = math.sqrt(disc)
		x1 = (-b + f1) / (2 * a)
		x2 = (-b - f1) / (2 * a)
		print(f"Two roots: {x1}, {x2}")

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
	main()

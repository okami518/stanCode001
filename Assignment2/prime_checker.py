"""
File: prime_checker.py
Name: Kang
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	print('Welcome to the prime checker!')
	while True:
		num = 3

		n = int(input('n: '))
		if n == EXIT:
			break
		elif n % 2 == 0:
			print(f"{n} is not a prime number.")
			break
		else:
			while True:
				if n % num == 0:
					if n == num:
						print(f"{n} is a prime number.")
						break
					else:
						print(f"{n} is not a prime number.")
						break
				else:
					num += 1

	print('Have a good one!')


if __name__ == "__main__":
	main()

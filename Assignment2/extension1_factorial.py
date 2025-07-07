"""
File: extension1_factioral.py
Name:  Kang
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	print('Welcome to stanCode factorial master!')
	while True:
		n = int(input('Gie me a number, and I will list the answer of factorial: '))
		if n == EXIT:
			break
		else:
			a = 1  # 只能用１，因為１乘以任何數才會變第一個數
			for i in range(n, 0, -1):
				a *= i  # 讓a不斷刷新成上一次運算的結果
			print(a)

	print('- - - - - - See ya! -------------')

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
	main()
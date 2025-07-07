"""
File: weather_master.py
Name: Kang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	print(f"stanCode \"Weather Master 4.0\"!")
	highest = -float('inf')  # Initialize highest temperature
	lowest = float('inf')  # Initialize lowest temperature
	days = 0  # Count of valid days
	total = 0  # Sum of temperatures
	cold_days = 0  # Count of cold days (below 16°C)
	while True:
		data = int(input(f"Next Temperature: (or {EXIT} to quit)?"))
		if data == EXIT:
			break
		else:
			days += 1
			total += data
			if data < 16:
				cold_days += 1
			if data > highest:
				highest = data  # Update highest temperature
			if data < lowest:
				lowest = data  # Update lowest temperature
	print(f"Highest temperature = {highest}")
	print(f"lowest temperature = {lowest}")
	print(f"Average = {total/days}")
	print(f"{cold_days} cold day(s)")







# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()

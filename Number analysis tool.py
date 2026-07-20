numbers = []

while True:
    user_input = input("Enter a number (or type 'stop'): ")

    if user_input.lower() == "stop":
        break
    elif user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        numbers.append(int(user_input))
    else:
        print("Invalid input, try again.")
# above code creates a list of numbers that can be changed by user input.
# user can add as many numbers as they want until they break the loop using 'stop'
count_over_16 = 0
count_even = 0
count_negative = 0
# creates a data set that adds 1 for either 3 conditions
for x in numbers:
	if x > 16:
		count_over_16 += 1
	if x % 2 == 0:
		count_even += 1
	if x < 0:
		count_negative += 1

average = sum(numbers) / len(numbers)

if count_over_16 > 5:
	print("Lots of big numbers")
elif count_over_16 == 0:
	print("All numbers were 16 or below")
else:
	print(" Nice range of values")

print(f'Even numbers: {count_even}')
print(f'Negative numbers: {count_negative}')

if numbers:
	print(f'The highest number is: {max(numbers)}')
	print(f'The lowest number is: {min(numbers)}')
	print(f'The average is: {average}')
else:
	print('No numbers were entered.')
# prints the analysis of the numbers for the user to see
# if there are no numbers, user gets a message saying no numbers were entered
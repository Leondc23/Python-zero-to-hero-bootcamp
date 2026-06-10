temp = [12,15,18,21,17,14]
average_temp = (sum(temp)/len(temp))#using the len() function to retrieve the length of the list so if the length changes, the equation will still work to find an average.
print(f"the average temperature was: {average_temp:.2f} Degrees Celcius.")# using an fstring to format the string
print(min(temp), "Degrees Celcius was the lowest recorded temperature")
print(max(temp), "Degrees Celcius was the highest recorded temperature")

count = 0 #creating a new variable and setting the value to 0

for degree in temp: #creating a loop that counts the number of temperatures that are above 16 degrees
	if degree > 16:
		count += 1  #adds 1 to the variable count for every value above 16

print(f'the number of days that reach a temperature above 16 degrees is: {count}') #an fstring used to format the string and insert the count at the end
		
		


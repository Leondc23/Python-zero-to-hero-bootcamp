temp = [12,15,18,21,17,14]
average_temp = (sum(temp)/len(temp))#using the len() function to retrieve the length of the list so if the length changes, the equation will still work to find an average.
print(f"the average temperature was: {average_temp:.2f} Degrees Celcius.")# using an fstring to format the string
print(min(temp), "Degrees Celcius was the lowest recorded temperature")
print(max(temp), "Degrees Celcius was the highest recorded temperature")

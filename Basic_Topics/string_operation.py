input_string = "Hello World"

print("You entered: ", input_string)
print(input_string[::-1])

print(input_string[3:0:-1])

print(input_string.split(" "))

joined_string = " ".join(input_string.split(" "))
print(joined_string)
# Write a program to accept a string from the user and display characters that are present at an even index number.

# Pseudo code


# Ask user input for a string
string = input("What is your desired string?: ")
length = len(string)

# Write somethign to separate the even index number of the string and print the characters
for i in range(0, length, 2):
    print(string[i])


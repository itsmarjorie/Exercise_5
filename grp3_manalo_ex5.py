# Calculate the length of a string

text = input("Enter a string: ")

length = len(text)

print("Length of the string is:", length)

# Count the number of characters in a string

text = input("Enter a string: ")

count = 0
for char in text:
  count = count + 1

print("Number of characters:", count)

# Replace all occurrences of the first character with $

text = input("Enter a string: ")

first_char = text[0]

new_string = first_char + text[1:].replace(first_char, '$')

print("Result:", new_string)

# Swap first two characters of two strings

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

result = new_str1 + " " + new_str2

print("Result:", result)

# Concatenate 4 variables

a = "I"
b = "LOVE"
c = "YOU"
d = "SO MUCH"

sentence = a + " " + b + " " + c + " " + d

print(sentence)

# Concatenate two strings from user input

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1 + " " + str2

print("Concatenated string:", result)

# Name and age in a paragraph

name = "Marjorie Manalo"
age = "18"

paragraph = "My name is " + name + " and I am " + age + " years old. I am currently studying and learning Python programming."

print(paragraph)

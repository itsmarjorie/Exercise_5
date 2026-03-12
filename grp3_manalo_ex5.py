text = "Marjorie B. Manalo"

length = len(text)

print("The length of the string is:", length)

print()

text = "BSIT - 1V"

count = 0
for char in text:
    count += 1

print("Total number of characters:", count)

print()

text = "Sya lang"

first_char = text[0]

new_string = first_char + text[1:].replace(first_char, '$')

print("Modified string:", new_string)

print()

str1 = "Marjorie"
str2 = "Manalo"

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

print("Result:", new_str1 + " " + new_str2)

print()

a = "I"
b = "MISS"
c = "YOU"
d = "SO MUCH"

result = a + " " + b + " " + c + " " + d

print(result)

print()

first_str = "Sya lang po"
second_str = "ang mahal ko"

result = first_str + " " + second_str

print("Concatenated string:", result)

print()

name = "Marjorie B. Manalo"
age = "18"

paragraph = "My name is " + name + " and I am " + age + " years old. I am currently studying programming and learning Python."

print(paragraph)

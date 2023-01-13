 # Display a string literal with the print() function
print('Hello')

# Assign String to a Variable
a = "Hello"
print(a)

# === Multiline Strings ===
# Three double quotes
string_double_quotes = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(string_double_quotes)

# Three single quotes
string_single_quotes = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(string_single_quotes)

# === Slicing ===
slicing = "Hello, World!"
print(slicing[2:5])

# Slice From the Start
slice_from_the_start = "Hello, World!"
print(slice_from_the_start[:5])

# Slice To the End
slice_from_the_end = "Hello, World!"
print(slice_from_the_end[2:])

# === Modify Strings ===
# Upper Case
upper_case = "Hello, World!"
print(upper_case.upper())

# Lower Case
lower_case = "Hello, World!"
print(lower_case.upper())

# Replace String
# The replace() method replaces a string with another string
replace_string = "Hello, World!"
print(replace_string.replace("H", "J"))

# Split String
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# === String Concatenation ===
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c) # return HelloWorld

# === String Format ===
# We can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

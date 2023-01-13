# === While loops ===
# With the while loop we can execute a set of statements as long as a condition is true.
# Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1

# The break Statement
# Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# The continue Statement
# Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# The else Statement
# Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# === For Loops ===
# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String
# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# The break Statement
# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

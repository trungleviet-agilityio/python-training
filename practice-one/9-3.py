# Write a function named avoids that takes a word and a string
# of forbidden letters, and that returns True if the word doesnot
# use any of the forbidden letters.
def avoids(word, string):
  for letter in word:
    if letter in string:
      return False

  return True

print(avoids('trung', 'ttt')) # => False
print(avoids('trung', 'aaa')) # => True

# Modify your program to prompt the user to enter a string of
# forbidden letters and then print the number of words that
# dont contain any of them.
string = str(input('Please enter the string of forbidden letters:\n'))

fin = open('words.txt')
count = 0
for word in fin:
  word = word.strip()
  if avoids(word, string):
    count += 1
    print(word)

print('The total number of words that donot contain any letter from "{}" is {}'.format(string, count))

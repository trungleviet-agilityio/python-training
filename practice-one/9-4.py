# Write a function named uses_only that takes a word and a string
# of letters, and that returns True if the word contains only
# letters in the list.
def uses_only(word, string):
  for letter in word:
    if letter not in string:
      return False

  return True

print(uses_only('trung', 'trg')) # => False
print(uses_only('trung', 'trung')) # => True

# Can you make a sentence using only the letters acefhlo?
# Other than Hoe alfalfa?
string = 'acefhlo'
fin = open('words.txt')
count = 0
for line in fin:
  word = line.strip()
  if word != 'hoe' and word != 'alfalfa':
    count += 1
    print(word)

print('You have {} words which contain only "acefhlo" letters to make a sentance.'.format(count))
# result = 113781 words

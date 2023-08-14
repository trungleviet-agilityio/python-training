# Write a function called has_no_e that returns True if
# the given word does not have the letter e in it.
def has_no_e(word):
  word = word.lower()
  for letter in word:
    if letter == 'e':
      return False

  return True

print(has_no_e('test'))

# Modify your program ex_9_1 from the previous section to
# print only the words that have no e and compute
# the percentage of the words in the list have no e.
fin = open('words.txt')
total_words = 0
no_e_words = 0

for word in fin:
  word = word.strip()
  total_words += 1

  if has_no_e(word):
    no_e_words += 1
    print(word)

# print(total_words, no_e_words)
print('the percentage of the words in the list have no e: {0:2f}%'.format(no_e_words/total_words*100))
# result = 33.063814%

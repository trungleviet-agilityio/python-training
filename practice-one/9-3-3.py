# Can you find a combination of 5 forbidden letters that
# excludes the smallest number of words?

import time

# Create a string of all words form words.txt
def build_string():
  string = ''
  fin = open('words.txt')
  for line in fin:
    word = line.strip()
    string = string + word

  return string

def words_frequency():
  '''
    This function calculates letters
    frequency and returns it as a dictionary
  '''
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  string = build_string()
  dictionary = {}
  for i in alphabet:
    dictionary[i] = dictionary.get(i, string.count(i))

  return dictionary

def words_popularity():
  '''
    This function returns the 5 most
    rarely-used words in the text
  '''
  dictionary = words_frequency()
  print('dictionary', dictionary)

  dict_copy = dictionary
  counter = 0
  popular_words = []
  while counter < 5:
    popular_word = min(dict_copy, key=dict_copy.get)
    popular_words.append(popular_word)
    dict_copy.pop(popular_word, None)
    counter += 1

  return popular_words

start_time = time.time()
print('The 5 most rarely-used words in the text: {}'.format(words_popularity()))
function_time = time.time() - start_time

print('Running time is {0:.4f} s'.format(function_time))

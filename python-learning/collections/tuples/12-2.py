# In this example, ties are broken by comparing words, so words
# with the same length appear in reverse alphabetical order. For
# other applications you might want to break ties at random.
# Modify this example so that words with the same length appear
# in random order. 
import random

def sort_by_length(words):
  t = []
  for word in words:
    t.append((len(word), random.random(), word))
      
  t.sort(reverse=True)
  res = []
  
  for length, _, word in t:
    res.append(word)
  return res

print(sort_by_length(['le', 'viet', 'trung']))

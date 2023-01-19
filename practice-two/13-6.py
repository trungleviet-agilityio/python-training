# write a program that uses set subtraction to find words in the 
# book that are not in the word list. 
import string, time

def book_words():
  '''
    This function reads file (book), breaks it into
    a list of used words in lower case.
  '''
  book = open('tsawyer.txt', 'r')
  text = book.read().replace('\n', '')
  words_list = ''.join(c.lower() for c in text if c not in string.punctuation).split()
  #print(text)
  book.close
    
  return words_list

def words_list():
  '''
    This function returns words list from words.txt file.
  '''
  res = []
  fin = open('words.txt')
  for line in fin:
    word = line.strip()
    res.append(word)
  return res

def avoids():
  set1 = set(book_words())
  set2 = set(words_list())
  res = set1 - set2
  print('In total there are {} words which are not in words.txt file'.format(len(res)))

start_time = time.time()
avoids()
function_time = time.time() - start_time

print('Running time is {0:.4f} s'.format(function_time))

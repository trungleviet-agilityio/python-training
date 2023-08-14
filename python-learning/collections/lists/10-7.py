# Two words are anagrams if you can rearrange the letters
# from one to spell the other. Write a function called
# is_anagram that takes two strings and returns True if they
# are anagrams.
def is_anagram(listik1, listik2):
  if len(listik1) == len(listik2):
    listik1 = list(listik1)
    listik2 = list(listik2)
    listik1.sort()
    listik2.sort()
    return listik1 == listik2
  else:
    return False

print(is_anagram('trung','turng'))
print(is_anagram('trung','trunh'))
print(is_anagram(' ',' '))

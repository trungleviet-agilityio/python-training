# Use capitalize_all to write a function named capitalize_nested
# that takes a nested list of strings and returns a new nested
# list with all strings capitalized.
def capitalize_nested(listik):
  capitalized = []
  for i in listik:
    if type(i) is list:
      i = capitalize_nested(i)
    else:
      i = i.capitalize()
    capitalized.append(i)
  return capitalized

print(capitalize_nested(['a','b','c',['a','a'],['a']]))
print(capitalize_nested([['banana'],['apple'],['cucumber'],['orange'],['lime'],['tomato']]))

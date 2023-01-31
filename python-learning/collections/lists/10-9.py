# Write a function called remove_duplicates that takes a list
# and returns a new list with only the unique elements from the
# original. Hint: they do not have to be in the same order.
def remove_duplicates(listik):
  res = []
  for i in listik:
    if i not in res:
        res.append(i)
  return res

print(remove_duplicates(['l','i','s','t','i','k']))
print(remove_duplicates([1,1,1,2,0,2]))

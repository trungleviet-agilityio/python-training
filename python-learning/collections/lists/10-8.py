# Write a function called has_duplicates that takes a list and
# returns True if there is any element that appears more than
# once. It should not modify the original list.
def has_duplicates(listik):
  for i in listik:
    if listik.count(i)> 1:
        return True
  return False

print(has_duplicates([1, 2, 3, 2, 4]))
print(has_duplicates([1, 2, 3, 0, 4]))

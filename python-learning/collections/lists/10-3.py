# Write a function that takes a list of numbers and returns
# the cumulative sum; that is, a new list where the ith element
# is the sum of the first i + 1 elements from the original list.
# For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
def nested_sum(listik):
  total = 0
  res = []
  for i in listik:
      total += i
      res.append(total)
  return res

print(nested_sum([1,2,3]))
print(nested_sum([]))
print(nested_sum([-1,1,2,0]))
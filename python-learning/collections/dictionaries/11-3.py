# Dictionaries have a method called keys that returns the keys
# of the dictionary, in no particular order, as a list.
# Modify print_hist to print the keys and their values in
# alphabetical order.
def histogram(s):
  d = dict()
  for c in s:
    d[c] = d.get(c, s.count(c))
  return d

def print_hist(h):
  listik = sorted(h.keys())
  for i in listik:
    print(i, h[i])

h = histogram('brontosaurus')
print_hist(h)

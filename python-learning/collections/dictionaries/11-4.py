# Modify reverse_lookup so that it builds and returns a list
# of all keys that map to v, or an empty list if there are none.
def histogram(s):
  d = dict()
  for c in s:
    d[c] = d.get(c, s.count(c))
  return d

def reverse_lookup(d, v):
  res = []
  for k in d:
    if d[k] == v:
      res.append(k)

  return res

h = histogram('leviettrung')
print(reverse_lookup(h, 2)) # ['e', 't']
print(reverse_lookup(h, 3)) # []
print(reverse_lookup(h, 1)) # ['l', 'v', 'i', 'r', 'u', 'n', 'g']

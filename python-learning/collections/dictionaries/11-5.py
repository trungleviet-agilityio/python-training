def histogram(s):
  d = dict()
  for c in s:
    d[c] = d.get(c, s.count(c))
  return d

def invert_dict(d):
  inverse = dict()
  for k, v in d.items():
    inverse.setdefault(v, []).append(k)
  return inverse

hist = histogram('leviettrung') # {1: ['l', 'v', 'i', 'r', 'u', 'n', 'g'], 2: ['e', 't']}
print(invert_dict(hist))

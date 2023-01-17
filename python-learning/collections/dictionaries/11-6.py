# Run this version of fibonacci and the original with a range
# of parameters and compare their run times.
import time

known = {0:0, 1:1}

def fibonacci1(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci1(n-1) + fibonacci1(n-2)

def fibonacci2(n):
  if n in known:
    return known[n]
  res = fibonacci2(n-1) + fibonacci2(n-2)
  known[n] = res

  return res

start_time = time.time()
fibonacci1(30)
function_time1 = time.time() - start_time

start_time = time.time()
fibonacci2(30)
function_time2 = time.time() - start_time

print('fibonacci 1:', function_time1)
print('fibonacci 2:', function_time2)

# The ogriginal one takes much more time

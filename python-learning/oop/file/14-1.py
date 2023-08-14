import string

def sed(filename1, filename2, pattern, replacement):
    
  try:
    fin = open(filename1, 'r')
    fout = open(filename2, 'w')

    for line in fin:
      fout.write(line.replace(pattern, replacement))

    fout.close()

  except:
    print("That didn't go as planned...")

sed('test1.txt', 'test2.txt', 'et', 'zzzz')

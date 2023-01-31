"""__str__() and __repr__()
Examples Using a Built-In Class
"""
import datetime

my_date = datetime.datetime.now()

print("__str__() string: ", my_date.__str__())
print("str() string: ", str(my_date))
# __str__() string:  2023-01-31 09:29:33.399695
# str() string:  2023-01-31 09:29:33.399695

print("__repr__() string: ", my_date.__repr__())
print("repr() string: ", repr(my_date))
# __repr__() string:  datetime.datetime(2023, 1, 31, 9, 29, 33, 399695)
# repr() string:  datetime.datetime(2023, 1, 31, 9, 29, 33, 399695)

"""Use the repr() function with the eval() function
to create a new object from the string
"""
my_date_1 = datetime.datetime.now()
my_date_2 = eval(repr(my_date_1))

print("my_date_1 repr() string: ", repr(my_date_1))
print("my_date_2 repr() string: ", repr(my_date_2))
# my_date_1 repr() string:  datetime.datetime(2023, 1, 31, 9, 35, 5, 289791)
# my_date_2 repr() string:  datetime.datetime(2023, 1, 31, 9, 35, 5, 289791)

print("the values of the objects are equal: ", my_date_1==my_date_2) #True

"""__str__() and __repr__()
Examples Using a New Class
"""

# Class doesn’t implement the __str__() or __repr()__ methods
class Ocean:

  def __init__(self, sea_creature_name, sea_creature_age):
    self.name = sea_creature_name
    self.age = sea_creature_age

c = Ocean('Jellyfish', 5)

print(str(c)) # <__main__.Ocean object at 0x7f8939abbc70>
print(repr(c)) # <__main__.Ocean object at 0x7f8939abbc70>

# Update the Ocean class with implementations of the __str__() and __repr__() methods:
class NewOcean:
  def __init__(self, sea_creature_name, sea_creature_age):
    self.name = sea_creature_name
    self.age = sea_creature_age

  def __str__(self):
    return f'The creature type is {self.name} and the age is {self.age}'

  def __repr__(self):
    return f'Ocean(\'{self.name}\', {self.age})'

d = NewOcean('Jellyfish', 5)

print(str(d)) # The creature type is Jellyfish and the age is 5
print(repr(d)) # Ocean('Jellyfish', 5)

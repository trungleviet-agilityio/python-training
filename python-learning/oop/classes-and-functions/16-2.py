from __future__ import print_function, division

from datetime import datetime

def main():
  print("Today's date and the day of the week:")
  today = datetime.today()
  print(today)
  print(today.strftime("%A"))

  print("Your next birthday and how far away it is:")
  s = '12/19/1999' # Enter your birthday in mm/dd/yyyy format:
  bday = datetime.strptime(s, '%m/%d/%Y')

  next_bday = bday.replace(year=today.year)
  if next_bday < today:
    next_bday = next_bday.replace(year=today.year+1)
  print(next_bday)

  until_next_bday = next_bday - today
  print(until_next_bday)

  print("Your current age:")
  last_bday = next_bday.replace(year=next_bday.year-1)
  age = last_bday.year - bday.year
  print(age)

  print("For people born on these dates:")
  bday1 = datetime(day=19, month=12, year=1999)
  bday2 = datetime(day=9, month=12, year=2007)
  print(bday1)
  print(bday2)

  print("Double Day is")
  d1 = min(bday1, bday2)
  d2 = max(bday1, bday2)
  dd = d2 + (d2 - d1)
  print(dd)

if __name__ == '__main__':
  main()

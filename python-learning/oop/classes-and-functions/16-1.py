class Time:
	"""Represents the time of day.
	attributes: hour, minute, second
	"""

def print_time(t):
	print(('%.2d:%.2d:%.2d') % (t.hour, t.minute, t.second))

def int_to_time(seconds):
  """Makes a new Time object.
  seconds: int seconds since midnight.
  """
  time = Time()
  minutes, time.second = divmod(seconds, 60)
  time.hour, time.minute = divmod(minutes, 60)
  return time

def time_to_int(time):
  """Computes the number of seconds since midnight.
  time: Time object.
  """
  minutes = time.hour * 60 + time.minute
  seconds = minutes * 60 + time.second
  return seconds

def mul_time(t, n):
	return int_to_time(time_to_int(t) * n)

def average_pace(t, delta_x):
	""" Represents average pace in a race
	t: finishing time
	delta_x: movement during race
	unit : time per mile """
	return int_to_time(time_to_int(t) / delta_x )

if __name__ == '__main__':
	t = Time()
	t.hour = 3
	t.minute = 30
	t.second = 30
	print_time(mul_time(t, 3)) # Result: 10:31:30
	print_time(average_pace(t,30)) # Result: 00:07:01

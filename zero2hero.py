# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
  animal_list = list(text.split())
  if animal_list[0][0] == animal_list[1][0]:
    return True
  return False

print(animal_crackers('lion leopord'))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. 
# If not, return False
def makes_twenty(a, b):
  if 20 in [a, b]:
    return True
  elif a+b == 20:
    return True
  return False

print(makes_twenty(2, 18))


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# The first function will do the job but incase if the string provided is less than size 3, it will throw an error
# The version one (v1), will accepts any strings of length

def old_macdonald(text):
  text = text.capitalize()
  return text[:3]+text[3].upper()+text[4:]

def old_macdonald_v1(text):
  text = text.capitalize()
  if len(text) > 3:
    return text[:3]+text[3].upper()+text[4:]
  return text

print(old_macdonald('macdonald'))
print(old_macdonald_v1('mac'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# Here, you could use either list unpacking (*) or the join with space. Both yeilds the same.
def master_yoda(text):
  text_list = list(text.split())
  return text_list[::-1]

print(*master_yoda('Hey! Me Yoda'))   # List unpacking
print(' '. join(master_yoda('Hey! Me Yoda')))  # Joining list with the space


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
  if abs(n-100) < 11 or abs(n-200) < 11:
    return True
  return False

print(almost_there(200))

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# I have given two solutions, one acheived via passing as a list, another via arguments
def has33(text):
  px = 0
  for x in text:
    if [3, 3] == [px, x]:
      return True
    px = x
  return False

print(has33([3, 0, 3, 3]))

def has33_v1(*args):
  px = 0
  for x in args:
    if [3, 3] == [px, x]:
      return True
    px = x
  return False

print(has33_v1(3, 0, 0, 3))

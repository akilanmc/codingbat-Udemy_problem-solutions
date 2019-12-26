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

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
  paperdoll = ''
  for x in text:
    paperdoll += x*3
  return paperdoll

print(paper_doll('hey'))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, 
# if the sum (even after adjustment) exceeds 21, return 'BUST
def blackjack(*args):
  args_sum = sum(args)
  if args_sum <= 21:
    return args_sum
  elif 11 in args:
    if args_sum - 10 <= 21:
      return args_sum - 10
  return 'BUST'

print(blackjack(11, 10, 11))

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers
def summer_69(nums):
  sum_num = 0
  skip = 0
  for x in nums:
    if skip == 0 and x != 6:
      sum_num += x
    elif x == 6:
      skip = 1
    elif x == 9:
      skip = 0
  return sum_num

print(summer_69([2, 1, 6, 9, 11]))

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# As per the problem statement, 007 can be present in non sequenctially but if it needs to be present in 
# Sequential mannner, disable the else comment section. That will do the job
def spy_game(nums):
  px = 1
  ppx = 1
  for x in nums:
    if x == 7 and px == 0 and ppx == 0:
      return True
    elif x == 0 and px == 1:
      px = 0
    elif x == 0 and px == 0:
      ppx = 0
    #else:
      #px = 1
      #ppx = 1
  return False

print(spy_game([1,2,4,0,0,1,5]))

def count_prime(num):
  prime = True
  for x in range(2,num):
    if num % x == 0:
      prime = False
  return prime

print(count_prime(11))

# Return the number of times that the string "code" appears anywhere in the given string variable (text),
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.

text = 'testing_code'
i = 0
count = 0
for x in text:
    # Check for the length of the remaining string is at least the size of search word (code)
    if len(text)-i >= 4 and text[i:i+2] + text[i+3] == 'coe':
        count = count + 1
    i += 1
print(count)

# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period
# So "xxyz" counts but "x.xyz" does not.

xyz_string = 'abc.xyzxyz'
dot_list = xyz_string.split('.')  # Split all the texts by period wise
xyz_check = False
i = 0
for x in dot_list:
    if i == 0:  # This section is meant for the first block of string, as it is not prefixed by a .dot Eg.'xyz.abc'
        i += 1
        if 'xyz' in x:
            xyz_check = True
    elif 'xyz' in x[1:]:
        xyz_check = True
print(xyz_check)

# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars.
# Return -1 if it can't be done

small = 9
big = 3
goal = 18
big_required = int(goal/5)  # Computing no. of big bars required in completing the goal
if big >= big_required:
    small_required = goal - (big_required * 5)  # Shedding out extra big bars available from the goal
else:
    small_required = goal - (big * 5)  # Shedding out given big bars from the goal

if small >= small_required:  # Checking the available small bars to met the goal requirement
    print(small_required)
else:
    print(-1)

# List 2 section

# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1
nums = [2, 1, 2, 3, 4]
count = 0
for x in nums:
    if x % 2 == 0:
        count += 1
print(count)

# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
# Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values

nums = [10, 3, 5, 6]
maxv = max(nums)
minv = min(nums)
print(maxv-minv)

# Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value,
# ignore just one copy, and likewise for the largest value. Use int division to produce the final average.
# You may assume that the array is length 3 or more.

lt = [-10, -4, -2, -4, -2, 0]
minv = min(lt)
maxv = max(lt)
sumv = sum(lt)-minv-maxv
print(int(sumv/(len(lt)-2)))

# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky,
# so it does not count and numbers that come immediately after a 13 also do not count

nums = [1, 2, 2, 1, 13]
# Initialize variables
sum_list = 0
px = 0

for x in nums:
    if x != 13 and px != 13:    # Skip the summation if the current & previous value is 13
        sum_list += x
        px = 0                  # Reset the previous value of 13 if set any
    elif px == 13 and x != 13:  # Reset the previous value of 13 if the current value is not 13
        px = 0
    elif x == 13:               # If current value is 13, assign 13 to previous x (px) variable
        px = x

print(sum_list)

# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
# and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

nums = [1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]
sum67 = 0
skip = 0

for x in nums:
    if x != 6 and skip == 0:
        sum67 += x
    elif x == 6:
        skip = 1
    elif x == 7:
        skip = 0

print(sum67)

# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere

nums = [4, 2, 4, 2, 2, 5]
px = 0
has22 = False

for x in nums:
    if x == 2 and px == 2:
        has22 = True
        break
    else:
        px = x

# Given a non-empty string like "Code" return a string like "CCoCodCode"

text = 'Code'
print(has22)

i = 0
sum_str = ''

while i < len(text):
    sum_str = sum_str + text[0:i + 1]
    i += 1

print(sum_str)

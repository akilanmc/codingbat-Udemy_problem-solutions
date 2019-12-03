# Each Problem has many solutions, presenting just one of them here. 

# Return the number of times that the string "code" appears anywhere in the given string variable (text),
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.

text = 'testing_code'
i = 0
count = 0
for x in text:
    # Check for the length of the remaining string is at least the size of search word (code)
    if len(text)-i >= 4 and text[i:i+2] + text[i+3] == 'coe':
        count = count +1
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

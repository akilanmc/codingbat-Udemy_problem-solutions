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

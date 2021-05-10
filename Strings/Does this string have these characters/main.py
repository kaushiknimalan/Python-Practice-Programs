wrd1 = input('Your 1st Word Here: ')
wrd2 = input('Your 2nd Word Here: ')
wrd1 = wrd1.lower()
wrd2 = wrd2.lower()
is_there = 0
is_not_there = 0

for letter in wrd2:
    if letter in wrd1:
        is_there += 1
    else:
        is_not_there += 1
print(f"The No.of Letters Which are There in The Word: {is_there} and The No.of Letters Which are Not There: {is_not_there}")


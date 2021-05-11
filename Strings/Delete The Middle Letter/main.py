word = input("Your Word: ")
i = 0
i1 = 0
index = len(word)//2
remainder_of_index = index % 2

if remainder_of_index == 0:
    while i <= index:
        if i == index:
            word = word.replace(word[i], "", 1)
            # break
        i += 1

elif remainder_of_index == 1:
    while i1 <= index:
        if i1 == index - 1:
            word = word.replace(word[i1], "", 1)
        if i1 == index - 1:
            word = word.replace(word[i1], "", 1)
            # break
        i1 += 1

print(word)

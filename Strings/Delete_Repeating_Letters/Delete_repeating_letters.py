
word = input("Your Word: ")
index = 0
while index <= len(word) - 1:
    ind = 0
    r_val = 0
    while ind < len(word) - 1:
        if word[ind] == word[index]:
            r_val += 1
        ind += 1

    if not r_val == 1 or r_val == 0:
        blank_space = ""
        word.replace(word[index], blank_space)
    index += 1
print(word)

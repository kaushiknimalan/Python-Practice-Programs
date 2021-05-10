
word = input("Your Word: ")
index = 0
while index <= len(word) - 1:
    ind = 0
    r_val = 0

    while ind <= len(word) - 1:
        if word[ind] == word[index]:
            r_val += 1
        ind += 1

    if not r_val == 1:
        word = word.replace(word[index], "")
    index += 1
print(word)

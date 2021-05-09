word = input("Your Word: ")
pal_word = word[::-1]

if word == pal_word:
    print(1)
else:
    print(0)

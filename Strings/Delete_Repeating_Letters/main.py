word = input("Your Word: ")


def find(letter):
    ind = 0
    r_val = 0
    while ind <= len(word)-1:
        if word[ind] == letter:
            r_val += 1
        ind += 1
    return r_val


def erase(letter, wrd):
    blank_space = ""
    wrd.replace(letter, blank_space)
    return wrd


def main():
    global word
    i = 0
    while i <= len(word)-1:
        num = find(word[i])
        if num > 1:
            word = erase(word[i], word)
        i += 1
    print(word)


if __name__ == '__main__':
    main()

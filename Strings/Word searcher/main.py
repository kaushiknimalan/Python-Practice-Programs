sentence = input('Your sentence here: ')
s_word = input('The word you wanna search: ')
sentence = sentence.lower()
s_word = s_word.lower()



def check(list_, word):
    index = 0
    check_ = True
    index_pos = 0
    spaces = len(list_) - 1
    crossed_spaces = 0
    the_no_of_wrds = len(list_)
    while index <= len(list_):
        try:
            if list_[index] == word:
                check_ = True
                the_no_of_wrds -= len(list_[index])
                break
            if not crossed_spaces == spaces:
                crossed_spaces += 1
            index_pos += len(list_[index])
            index += 1
        except IndexError:
            check_ = False
            break
    return check_, index_pos + the_no_of_wrds + crossed_spaces



c, ind, = check(sentence.split(' '), s_word)

if not c:
    print("Can't find your word anywhere in the sentence.")
elif c:
    print(f"String Found at {ind} index position")

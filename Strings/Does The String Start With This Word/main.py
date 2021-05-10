sentence = input("Your Sentence: ")
start_word = input("Your Guess: ")
word_list = sentence.split(' ')


def align_number(number):
    if number == 1:
        r_word = "st"
    elif number == 2:
        r_word = "nd"
    elif number == 3:
        r_word = "rd"
    else:
        r_word = "th"
    return r_word


def check():
    i = 0
    for word in word_list:
        if word == start_word:
            break
        i += 1
    return i + 1


if start_word == word_list[0]:
    print('True!! It is correct!!')
else:
    in_word = check()
    print(f"False!! It wasn't the Starting word!! It was in the {in_word}{align_number(in_word)} word in the sentence..")

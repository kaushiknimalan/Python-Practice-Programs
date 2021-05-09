sentence = input("Your sentence: ")
articles = ['a', 'an', 'the']
p_word = " "


def add_next_word(word1):
    global p_word
    p_word = p_word + word1 + " "


def main():
    i = 0

    for word in sentence.split(' '):
        if word in articles:
            add_next_word(sentence.split(' ')[i + 1])
        i += 1

    print(p_word)


if __name__ == "__main__":
    main()

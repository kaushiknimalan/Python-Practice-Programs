w_or_s = input("Your Word or Sentence: ")
letter = input('The Letter Which Should be Removed: ')

w_or_s = w_or_s.lower()
letter = letter.lower()
returning_word_or_sentence = w_or_s.replace(letter, '')
if returning_word_or_sentence == w_or_s:
    print('Letter Not Found')
else:
    print(returning_word_or_sentence)

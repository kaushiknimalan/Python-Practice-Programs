import random

# Opening and reading a txt file
with open("Words.Txt") as w:
    words = w.readlines()

no_of_letters = int(input('How Many Words you want?? '))

word_list = []

i = 0
while i <= no_of_letters:
    word_list.append(random.choice(words)[:-1])
    i += 1

true = False

while True:
    alpha_order_input = int(input("If you want the normal alphabetic order then type '0' else if you want the reversed order then type '1': "))
    if alpha_order_input == 0:
        true = True
        break
    elif alpha_order_input == 1:
        true = False
        break
    else:
        print(' ')
        print('You can only type 0 or 1')
        print(' ')
        continue

length_of_list = len(word_list)

print(' ')
print(f'The Words List Before: {word_list}')
print(' ')

ind = 0
while ind < length_of_list:
    index = 0
    while index < length_of_list - 1:
        if index == length_of_list - 1:
            no1 = word_list[index - 1]
            no2 = word_list[index]
        else:
            no1 = word_list[index]
            no2 = word_list[index + 1]

        if true:
            if no1 > no2:
                del word_list[index]
                del word_list[index]
                word_list.insert(index, no2)
                word_list.insert(index + 1, no1)
                print(word_list)

        elif not true:
            if no1 < no2:
                del word_list[index]
                del word_list[index]
                word_list.insert(index, no2)
                word_list.insert(index + 1, no1)
                print(word_list)

        index += 1

    ind += 1

print(' ')
print(f'The List But After: {word_list}')

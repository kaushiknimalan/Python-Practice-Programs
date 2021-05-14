import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
no_of_letters = int(input('How Many Words do you want?? '))
alpha_List = []
i = 0
while i <= no_of_letters:
    alpha_List.append(random.choice(letters))
    i += 1
print(' ')
print(f"The List: {alpha_List}")
print(' ')

alpha_order = False
while True:
    alpha_order_input = int(input("If you want the normal alphabetic order then type '0' else if you want the reversed order then type '1': "))
    if alpha_order_input == 0:
        alpha_order = True
        break
    elif alpha_order_input == 1:
        alpha_order = False
        break
    else:
        print(' ')
        print('You can only type 0 or 1')
        print(' ')
        continue


def get_ascii_number(list_):
    ascii_val_list = []
    for letter in list_:
        ascii_val_list.append(ord(letter))
    return ascii_val_list


def get_letter_format(list__):
    letter_val_list = []
    for number in list__:
        letter_val_list.append(chr(number))
    return letter_val_list


ascii_numbers = get_ascii_number(alpha_List)

ind = 0
while ind < len(ascii_numbers):
    index = 0
    while index < len(ascii_numbers) - 1:
        if index == len(ascii_numbers) - 1:
            no1 = ascii_numbers[index - 1]
            no2 = ascii_numbers[index]
        else:
            no1 = ascii_numbers[index]
            no2 = ascii_numbers[index + 1]

        if alpha_order:
            if no1 > no2:
                del ascii_numbers[index]
                del ascii_numbers[index]
                ascii_numbers.insert(index, no2)
                ascii_numbers.insert(index + 1, no1)
                print(get_letter_format(ascii_numbers))

        elif not alpha_order:
            if no1 < no2:
                del ascii_numbers[index]
                del ascii_numbers[index]
                ascii_numbers.insert(index, no2)
                ascii_numbers.insert(index + 1, no1)
                print(get_letter_format(ascii_numbers))

        index += 1

    ind += 1

length_of_list = int(input('How Many Numbers are you gonna enter?? '))

num_Array = []
i = 1
while i <= length_of_list:
    num_Array.append(int(input('Your number: ')))
    i += 1
ascending = bool(
    input('Enter True if you want this in Ascending order or Just leave it blank if you want it in Descending order: '))
no1 = 0
no2 = 0


def inspect_and_change(true):
    global num_Array
    global length_of_list
    global no1
    global no2

    print(f'Before : {num_Array}')
    print(' ')

    ind = 0
    while ind < length_of_list:
        index = 0
        while index < length_of_list - 1:
            if index == length_of_list - 1:
                no1 = num_Array[index - 1]
                no2 = num_Array[index]
            else:
                no1 = num_Array[index]
                no2 = num_Array[index + 1]

            if true:
                if no1 > no2:
                    del num_Array[index]
                    del num_Array[index]
                    num_Array.insert(index, no2)
                    num_Array.insert(index + 1, no1)
                    print(num_Array)

            elif not true:
                if no1 < no2:
                    del num_Array[index]
                    del num_Array[index]
                    num_Array.insert(index, no2)
                    num_Array.insert(index + 1, no1)
                    print(num_Array)

            index += 1

        ind += 1


inspect_and_change(ascending)

print(' ')
print(f'After: {num_Array}')


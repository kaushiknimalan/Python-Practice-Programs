number = int(input('The Number: '))
number = str(number)

even_int_list = []
answer = 0
integer = 0
i = 0
while i <= len(number) - 1:
    integer = int(number[i])
    if integer % 2 == 0:
        even_int_list.append(integer)
        answer += integer
    i += 1


print(f'The Sum of the Even Integers in Number {number} = {answer}')

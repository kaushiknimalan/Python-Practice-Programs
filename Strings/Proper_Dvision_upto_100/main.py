

def get_divisor(num):
    divisor_list = []
    ind = 1

    while ind <= num:
        rem = num % ind
        if rem == 0:
            divisor_list.append(ind)
        ind += 1
    return divisor_list


len_of_g_list = len(get_divisor(10))
len_list = 0
div_list = []
i = 1
while i <= 100:
    if not i > 10:
        print(f'{i} = {get_divisor(i)}')
    elif i >= 10:
        len_list = len(get_divisor(i))
        if len_list >= len_of_g_list:
            len_of_g_list = len_list
            div_list = get_divisor(i)

    i += 1

print(f'{i-1} = {get_divisor(i-1)}')

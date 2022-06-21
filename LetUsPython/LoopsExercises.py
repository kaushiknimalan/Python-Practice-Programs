def number_reversed(number):
    no = number
    number = str(number)
    number = list(number)
    j = ""

    number.reverse()
    reverse = j.join(number)
    reverse = int(reverse)

    if no == reverse:
        print("Both the numbers are same.")
    else:
        print("Both numbers are not same.")


def number_reversed_repetition(number):
    no = number
    number = str(number)
    number = list(number)
    reverse = []
    i = len(number)-1
    while i >= 0:
        reverse.append(number[i])
        i -= 1
    j = ""
    reverse = int(j.join(reverse))
    if no == reverse:
        print("Both the numbers are same.")
    else:
        print("Both numbers are not same.")


number_reversed_repetition(1001)
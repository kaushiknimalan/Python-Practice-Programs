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


def factorial(number):
    i = 1
    ans = 1
    while i <= number:
        ans *= i
        i += 1
    print(ans)

def armstrong(till):
    ans = 0
    i_ = 0
    while i_ < till:
        for i in str(i_):
            i_in = int(i)
            ans += pow(i_in, 3)

        if ans == int(i_):
            print(ans)
        ans = 0
        i_ += 1



armstrong(10000)

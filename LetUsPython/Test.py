number = 10001
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

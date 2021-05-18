month_31_list = [1, 3, 5, 7, 8, 10, 12]


def give_number_joiner(int_):
    if int_ == 1:
        r_text = "st"
    elif int_ == 2:
        r_text = "nd"
    elif int_ == 3:
        r_text = "rd"
    else:
        r_text = "th"
    return r_text


def get_input():
    dates = []
    i = 0
    while i <= 2:

        if i == 0:
            dates.append(int(input('The date: ')))
        elif i == 1:
            dates.append(int(input('The Month as number (ex: January = 1): ')))
        else:
            dates.append(int(input('The Year: ')))
        i += 1
    return dates


candidate_names = []
looped_times = int(input("How many candidate's date are you gonna give? "))
candi_dates = []
index = 1

while index <= looped_times:
    print(' ')
    print(f"The {index}{give_number_joiner(index)} Candidate: ")
    candidate_names.append(input('The Name of the Candidate: '))
    candi_dates.append(get_input())
    index += 1

is_date_true = []
is_month_true = []
is_year_true = []

ind = 0
j = 0
date = []


while j <= len(candi_dates) - 1:
    date = candi_dates[j]

    while ind <= len(candi_dates) + 1:
        if ind == 0:
            if date[ind] <= 22:
                is_date_true.append(True)
            else:
                is_date_true.append(False)

        elif ind == 1:
            if date[ind] in month_31_list:
                is_month_true.append(True)
            else:
                is_month_true.append(False)

        elif ind == 2:
            if date[ind] <= 1986:
                is_year_true.append(True)
            else:
                is_year_true.append(False)

        ind += 1
    ind = 0
    j += 1

print(' ')
k = 0
while k <= len(candi_dates) - 1:
    if is_date_true[k]:
        if is_month_true[k]:
            if is_year_true[k]:
                print(f'{candidate_names[k]} is eligible')
            else:
                print(f'{candidate_names[k]} is not eligible')
        else:
            print(f'{candidate_names[k]} is not eligible')

    else:
        print(f'{candidate_names[k]} is not eligible')
    k += 1

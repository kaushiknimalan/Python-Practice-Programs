looping_Times = int(input('How many numbers are you gonna give?? '))
num_array = []
ans = 0
i = 1
while i <= looping_Times:
    num_array.append(int(input(f'Your number: ')))
    i += 1
for number in num_array:
    ans += number

d2 = ans % 2
d3 = ans % 3
d5 = ans % 5

if d2 == 0 and d3 == 0 and d5 == 0:
    print(f'The Sum of all numbers = {ans}')
    print(' ')
    print(f'The sum of all the numbers divided by 2 = {ans//2}, By 3 = {ans//3}, By 5 = {ans//5}')
    print(f'And the corresponding remainders = {d2}, {d3}, {d5}')
    print(' ')
    print('So the answer is 0')
else:
    print(f'The Sum of all numbers = {ans}')
    print(' ')
    print(f'The sum of all the numbers divided by 2 = {ans // 2}, By 3 = {ans // 3}, By 5 = {ans // 5}')
    print(f'And the corresponding remainders = {d2}, {d3}, {d5}')
    print(' ')
    print('So the answer is 1')

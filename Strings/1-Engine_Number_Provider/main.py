word = input("All The Letters and Numbers Present on Your Car's Number Plate: ")
numbers = []

for lorN in word:
    is_numerical = lorN.isnumeric()
    if is_numerical:
        lorn = int(lorN)
        numbers.append(lorn)
i = 0
n1 = 0
num = 0


if len(numbers) > 1:
    while i <= len(numbers)-1:
        n1 = numbers[i]
        num += n1
        i += 1
    print(num)
else:
    print(numbers[0])

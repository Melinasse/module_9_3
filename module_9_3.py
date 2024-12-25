first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = zip(first, second)

first_result = [len(i) - len(y) for i, y in zp if len(i) != len(y)]
for elem in first_result:
    print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
# for elem in second_result:
print(list(second_result))

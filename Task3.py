# Task3! Sorting Dictionary by Key and Value
def sort_by_key(input_dic_):
    return dict(sorted(input_dic_.items(), key=lambda item: item[0]))


def sort_by_value(input_dic_):
    return dict(sorted(input_dic_.items(), key=lambda item: item[1]))


input_dic = {}

with open('task3.txt', 'r') as f:

    for line in f:
        key_value = line.split(' ')
        input_dic[key_value[0]] = int(key_value[1].strip())

print('Original Dictionary')
print(input_dic)
print()
print('By Key Sort')
print(sort_by_key(input_dic))
print()
print('By Value Sort')
print(sort_by_value(input_dic))


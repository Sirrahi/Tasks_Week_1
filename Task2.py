# Task2! Sorting Words Alphabetically in a List
def words_sort(words_list_):
    return sorted(words_list_, key=lambda word: word.lower())


words_list = []

with open('task2.txt', 'r') as f:
    for line in f:
        words_list.append(line.strip())

print(words_sort(words_list))

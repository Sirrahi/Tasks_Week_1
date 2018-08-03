# Task1! Words Finding in List
def words_finder(words_list_, req_word_):
    return bool([word == req_word_ for word in words_list_ if word == req_word])


words_list = []

with open('task1.txt', 'r') as f:
    for line in f:
        words_list.append(line.strip())

print(words_list)
req_word = input("Enter the Word you want to check in the List: ")
print(words_finder(words_list, req_word))



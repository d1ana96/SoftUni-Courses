number = int(input())
word = input()

list_all = list()
list_filtered = list()

for i in range(number):
    current_string = input()
    list_all.append(current_string)
    if word in current_string:
        list_filtered.append(current_string)

print(list_all)
print(list_filtered)


todo = ["" for index in range(11)]
command = input()

while command != "End":
    explode = command.split("-")
    priority = int(explode[0])
    note = explode[1]
    todo[priority] += note
    command = input()

final_todo = [note for note in todo if note != ""]
print(final_todo)

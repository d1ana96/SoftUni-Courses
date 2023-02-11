width = int(input())
length = int(input())

total_cake_pieces = width * length

command = input()
no_more_pieces = False

while command != "STOP":
    current_pieces = int(command)
    total_cake_pieces -= current_pieces
    if total_cake_pieces <= 0:
        no_more_pieces = True
        break
    command = input()

if no_more_pieces:
    print(f"No more cake left! You need {abs(total_cake_pieces)} pieces more.")
else:
    print(f"{total_cake_pieces} pieces are left.")

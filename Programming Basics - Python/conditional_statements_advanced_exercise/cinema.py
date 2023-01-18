film_type = input()
rows = int(input())
columns = int(input())

ticket_price = 0

if film_type == "Premiere":
    ticket_price = 12
elif film_type == "Normal":
    ticket_price = 7.50
elif film_type == "Discount":
    ticket_price = 5

total_income = ticket_price * (rows * columns)
print(f"{total_income:.2f} leva")


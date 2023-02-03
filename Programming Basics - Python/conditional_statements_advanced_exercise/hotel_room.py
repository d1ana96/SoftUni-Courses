month = input()
number_nights = int(input())
studio_price = 0
apartment_price = 0


if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < number_nights < 14:
        studio_price -= studio_price * 0.05
    elif number_nights > 14:
        studio_price -= studio_price * 0.3

elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if number_nights > 14:
        studio_price -= studio_price * 0.2

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if number_nights > 14:
    apartment_price -= apartment_price * 0.1

total_price_for_studio = number_nights * studio_price
total_price_for_apartment = number_nights * apartment_price

print(f"Apartment: {total_price_for_apartment:.2f} lv.")
print(f"Studio: {total_price_for_studio:.2f} lv.")

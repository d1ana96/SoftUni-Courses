quadrat_metres_being_grassed = float(input())
middle_price = quadrat_metres_being_grassed * 7.61
discount = middle_price * 0.18
final_price = middle_price - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")

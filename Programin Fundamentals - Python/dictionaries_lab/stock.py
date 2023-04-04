data = input().split()

available_products = {}

for index in range(0, len(data), 2):
    current_product = data[index]
    quantity = int(data[index + 1])
    available_products[current_product] = quantity

searched_products = input().split()

for current_searched_product in searched_products:
    if current_searched_product in available_products:
        print(f"We have {available_products[current_searched_product]} of {current_searched_product} left")
    else:
        print(f"Sorry, we don't have {current_searched_product}")



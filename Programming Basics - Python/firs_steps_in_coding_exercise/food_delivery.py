number_chicken_menu = int(input()) * 10.35
number_fish_menu = int(input()) * 12.40
number_vegetarian_menu = int(input()) * 8.15
mid_sum = number_chicken_menu + number_fish_menu + number_vegetarian_menu
price_for_desert = mid_sum * 0.2
total_sum = mid_sum + price_for_desert + 2.50
print(total_sum)

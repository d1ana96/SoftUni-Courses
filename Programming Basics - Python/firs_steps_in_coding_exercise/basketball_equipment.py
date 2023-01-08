annual_price_for_training = int(input())
shoes = annual_price_for_training - (annual_price_for_training * 0.4)
clothes = shoes - (shoes * 0.2)
ball = clothes / 4
accessories = ball / 5
total_sum = annual_price_for_training + shoes + clothes + ball + accessories
print(total_sum)

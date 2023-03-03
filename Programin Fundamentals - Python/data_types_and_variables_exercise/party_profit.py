companions_count = int(input())
days = int(input())
earnings_per_day = 0
total_earnings = 0


for day in range(1, days+1):
    if day % 10 == 0:
        companions_count -= 2
    if day % 15 == 0:
        companions_count += 5

    earnings_per_day = 50 - (companions_count * 2)

    if day % 3 == 0:
        earnings_per_day -= companions_count * 3
    if day % 5 == 0:
        earnings_per_day += companions_count * 20
        if day % 3 == 0:
            earnings_per_day -= companions_count * 2
    total_earnings += earnings_per_day

coins_per_companion = total_earnings // companions_count
print(f"{companions_count} companions received {coins_per_companion} coins each.")


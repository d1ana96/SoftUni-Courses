centuries = int(input())
years = centuries * 100
days = int(years * 365.2422) #защото по условие ни трябват само цели числа
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
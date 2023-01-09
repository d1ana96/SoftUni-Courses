total_pages_of_book = int(input())
pages_per_one_hour = int(input())
number_days = int(input())
total_hours_per_book = total_pages_of_book // pages_per_one_hour
needed_hours_per_day = total_hours_per_book // number_days
print(needed_hours_per_day)

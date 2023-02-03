exam_hour = int(input())
exam_minutes = int(input())
arriving_hour = int(input())
arriving_minutes = int(input())

on_time = True
is_early = False
delay_hours = 0
delay_minutes = 0
early_come = 0
early_hours = 0
early_minutes = 0

exam_time_in_minutes = exam_hour * 60 + exam_minutes
arriving_time_in_minutes = arriving_hour * 60 + arriving_minutes

if exam_time_in_minutes < arriving_time_in_minutes:
    on_time = False
    delay = arriving_time_in_minutes - exam_time_in_minutes
    delay_hours = delay // 60
    delay_minutes = delay % 60

elif arriving_time_in_minutes <= exam_time_in_minutes:
    early_come = exam_time_in_minutes - arriving_time_in_minutes
    early_hours = early_come // 60
    early_minutes = early_come % 60
    if 0 <= early_come <= 30:
        on_time = True
    elif early_come > 30:
        is_early = True


if not on_time:
    print("Late")
    if delay_hours == 0:
        print(f"{delay_minutes} minutes after the start")
    elif delay_hours > 0:
        if delay_minutes < 10:
            print(f"{delay_hours}:0{delay_minutes} hours after the start")
        else:
            print(f"{delay_hours}:{delay_minutes} hours after the start")

elif is_early:
    print("Early")
    if early_come >= 60:
        if early_minutes < 10:
            print(f"{early_hours}:0{early_minutes} hours before the start")
        else:
            print(f"{early_hours}:{early_minutes} hours before the start")
    else:
        print(f"{early_minutes} minutes before the start")


elif on_time:
    print("On time")
    if early_come == 0:
        pass
    else:
        print(f"{early_come} minutes before the start")

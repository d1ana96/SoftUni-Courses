bad_grades = int(input())
failed_times = 0
sum_grades = 0
solved_tasks_number = 0
last_task = ''
is_failed = False
task_name = input()

while task_name != "Enough":
    last_task = task_name
    grade = int(input())
    if grade <= 4:
        failed_times += 1
        if failed_times == bad_grades:
            is_failed = True
            print(f"You need a break, {failed_times} poor grades.")
            break

    solved_tasks_number += 1
    sum_grades += grade

    task_name = input()


average_grade = sum_grades / solved_tasks_number
if not is_failed:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {solved_tasks_number}")
    print(f"Last problem: {last_task}")

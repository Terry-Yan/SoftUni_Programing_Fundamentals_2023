happiness = [int(x) for x in input().split()]
improvement_factor = int(input())

employee_happiness = [(x * improvement_factor) for x in happiness]
average = sum(employee_happiness) / len(employee_happiness)
the_happy_bunch = [x for x in employee_happiness if x >= average]
happy_count = len(the_happy_bunch)
total_count = len(happiness)

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")

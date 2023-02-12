def perfect_check(x):
    sum_check = 0
    for num in range(1, x + 1):
        if x % num == 0:
            sum_check += num

    if sum_check == x * 2:
        return True


number = int(input())
perfect_flag = perfect_check(number)
if perfect_flag:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

def display_greater_than_n(numbers, n):
    for num in numbers:
        if num > n:
            print(num)


numbers_list = [5, 12, 8, 20, 15, 7, 3, 10]
n = 10
display_greater_than_n(numbers_list, n)
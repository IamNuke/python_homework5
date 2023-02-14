def my_sum(first_number: int, second_number: int) -> int:
    if second_number == 0:
        return first_number
    else:
        return my_sum(first_number + 1, second_number - 1)


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print(f'Result: {my_sum(a, b)}')

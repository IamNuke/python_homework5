def my_pow(number: int, degree: int) -> int:
    if degree == 1:
        return number
    else:
        return number * my_pow(number, degree - 1)


a = int(input("Enter number:"))
b = int(input("Enter degree:"))
print(f'Result: {my_pow(a, b)}')

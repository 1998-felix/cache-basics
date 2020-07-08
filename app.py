from timeit import default_timer

values = {

}


def timer(func):
    def inner(value):
        print(f'Calling {func.__name__} with value: {value}')
        start = default_timer()
        func(value)
        stop = default_timer()
        print(f"Executed {func.__name__} with {int(stop - start)} seconds")

    return inner


@timer
def factorial(num):
    if num == 0:
        return 1
    else:
        factorial_value = 1
        global values
        if num in values:
            factorial_value = values[num]
            print("in records")
        else:
            for i in range(1, num + 1):
                factorial_value = factorial_value * i
            else:
                values[num] = factorial_value

        return factorial_value


print(factorial(150000))
print(factorial(150000))

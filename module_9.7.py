def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res % 2 > 0 or res % 3 > 0 or res % 5 > 0:
            print('Простое')
        else:
            print('Составное')
        return res

    return wrapper


@is_prime
def sum_three(a: int, b: int, c: int):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

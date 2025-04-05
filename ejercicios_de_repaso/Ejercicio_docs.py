for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} es divisible por {x} * {n//x}")
            break
def divide (n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser zero.")
    return  n1 / n2

print(divide(2,1))

print(divide(2,0))
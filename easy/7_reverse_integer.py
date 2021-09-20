def reverse_integer(x):
    if x < 0:
        x = int(str(x)[0]+str(x)[1:][::-1])
        if x < -2**31:
            return 0
    else:
        x = int(str(x)[::-1])
        if x > 2**31 - 1:
            return 0

    return x

print(reverse_integer(123))
print(reverse_integer(-123))
print(reverse_integer(120))
print(reverse_integer(0))
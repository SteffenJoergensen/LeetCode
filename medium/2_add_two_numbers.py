def add_two_numbers(first, second):
    frst = 0
    for i, d in enumerate(first):
        frst += d * 10**i

    scnd = 0
    for i, d in enumerate(second):
        scnd += d * 10**i

    retval = [int(c) for c in str(frst + scnd)]
    retval.reverse()

    return retval

print(add_two_numbers([2, 4, 3], [5, 6, 4]))
print(add_two_numbers([0], [0]))
print(add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
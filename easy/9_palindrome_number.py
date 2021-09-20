def palindrome_number(x):
    x = str(x)

    return x[:int(len(x) / 2)] == x[int(len(x) / 2 + (len(x) % 2)):][::-1]

print(palindrome_number(121))
print(palindrome_number(-121))
print(palindrome_number(10))
print(palindrome_number(-101))
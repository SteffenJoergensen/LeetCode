def palindrome_number(x):
    x = str(x)

    return x == x[::-1]

print(palindrome_number(121))
print(palindrome_number(-121))
print(palindrome_number(10))
print(palindrome_number(-101))
roman_nums = {
    'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
    'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
}

def roman_to_integer(s):
    count = 0

    i = 0
    while i < len(s) - 1:
        if s[i:i+2] in roman_nums:
            count += roman_nums[s[i:i+2]]
            i += 2
        else:
            count += roman_nums[s[i]]
            i += 1

    if i < len(s):
        count += roman_nums[s[i]]

    return count

print(roman_to_integer("III"))
print(roman_to_integer("IV"))
print(roman_to_integer("IX"))
print(roman_to_integer("LVIII"))
print(roman_to_integer("MCMXCIV"))
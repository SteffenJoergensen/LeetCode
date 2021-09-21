def longest_common_prefix(strings):
    strings.sort(key=len)
    for i in range(len(strings[0])):
        for string in strings[1:]:
            if not strings[0][i] == string[i]:
                return strings[0][:i]

    return strings[0]

print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
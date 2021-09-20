def two_sum(nums, target):
    for i, frst in enumerate(nums):
        for j, scnd in enumerate(nums[i+1:]):
            if frst + scnd == target:
                return [i, j+i+1]

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
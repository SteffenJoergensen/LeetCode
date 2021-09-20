def two_sum(nums, target):
    for i, frst in enumerate(nums):
        for j, scnd in enumerate(nums[i+1:]):
            if frst + scnd == target:
                return [i, j+i+1]

def two_sum_hashing(nums, target):
    hash_table = {}
    for i in range(len(nums)):
        if target - nums[i] in hash_table:
            return [hash_table[target - nums[i]], i]
        else:
            hash_table[nums[i]] = i

print(two_sum_hashing([2, 7, 11, 15], 9))
print(two_sum_hashing([3, 2, 4], 6))
print(two_sum_hashing([3, 3], 6))
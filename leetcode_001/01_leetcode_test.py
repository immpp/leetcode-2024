def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        x = nums[i]
        for j in range(i + 1, n):
            y = nums[j]
            if x + y == target:
                return [i,j]
    return []

print(twoSum((3,2,3), 6))
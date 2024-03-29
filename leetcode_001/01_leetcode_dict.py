class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}

        for count, value in enumerate(nums):
            if target - value in dict:
                return [dict[target - value], count]
            dict[value] = count
        return []

print(Solution.twoSum([], (3,2,3), 6))
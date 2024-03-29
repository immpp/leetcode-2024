class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = []
        for num in nums:
            if target - num in nums:
                if len(nums) == 2:
                    ans = [0,1]
                    break
                elif target - num == num:
                    continue
                elif:
                    ans.append(nums.index(num))
        print(ans)

#Solution.twoSum([],(2,7,11,15),9)
#Solution.twoSum()
Solution.twoSum([],(3,3),6)
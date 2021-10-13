class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # for i,num in enumerate(nums):
        #     if target-num in nums[i+1:]:
        #         return [nums.index(num), nums[i+1:].index(target-num)+ (i+1)]
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target- num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]




nums = [2,7,11,15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))                
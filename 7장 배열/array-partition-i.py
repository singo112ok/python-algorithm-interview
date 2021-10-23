# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        nSum = 0
        for i in range(0, int(len(nums)/2)):
            nSum += nums[i*2]        
        return nSum
        
        


# nums = [1,4,3,2]
nums = [6,2,6,5,1,2]
sol = Solution()
print(sol.arrayPairSum(nums))                
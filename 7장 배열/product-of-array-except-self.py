# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        p = 1
        left = [1]
        for i in nums[:len(nums)-1]:
            p *= i
            left.append(p)

        p = 1 
        nums.reverse()
        right = [1]
        for i in nums[:len(nums)-1]:
            p *= i
            right.append(p)

        result = []
        for i in range(0, len(nums)):
            result.append(left[i]*right[len(nums)-1-i])
        
        return result
        
        


# nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
sol = Solution()
print(sol.productExceptSelf(nums))             
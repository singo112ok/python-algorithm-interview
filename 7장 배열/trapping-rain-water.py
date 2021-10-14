class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height)-1
        leftmax = height[left]
        rightmax = height[right]
        valume = 0
        while left < right:
            if leftmax < rightmax:
                left += 1
                if leftmax < height[left]:
                    leftmax = height[left]
                else:
                    valume += leftmax-height[left]
            else:
                right -= 1
                if rightmax < height[right]:
                    rightmax = height[right]
                else:
                    valume += rightmax-height[right]
        
        return valume

            



        


        


# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

sol = Solution()
print(sol.trap(height))                 
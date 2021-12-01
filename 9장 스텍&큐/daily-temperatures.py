# https://leetcode.com/problems/daily-temperatures/

from collections import defaultdict

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # for i in temperatures:
        #     if len(temp) == 0:
        #         temp.append(i)
        #         day.append(0)  
        #         continue
     
        #     for cnt, j in enumerate(day):
        #         day[cnt] = j+1                   
                      
        #     for j in range(0, len(temp)):
        #         if i > temp[-1]:
        #             temp.pop()
        #             result.append(day.pop())
        #             if len(temp) > 0:
        #                 if i <= temp[-1]:
        #                     break        

        #     temp.append(i)
        #     day.append(0)        
        #                   
        result = [0] * len(temperatures)
        stack = []      
        for i, cur in enumerate(temperatures):
            while stack and cur> temperatures[stack[-1]]:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)


        return result                 




temperatures = [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures(temperatures))              
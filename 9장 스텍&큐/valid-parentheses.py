# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets ={
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for i in s:
            if i in brackets:
                stack.append(brackets.get(i))            
            else:
                if len(stack) > 0:
                    if i == stack.pop():
                        continue
                    else:
                        return False
                else:
                    return False
        return True




        
        
# prices = "()[]{}"
prices = "(]"
sol = Solution()
print(sol.isValid(prices))                   
# https://leetcode.com/problems/remove-duplicate-letters/

from typing import Collection, Counter

import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # only : list = []
        # overlap : list = []
        # for i in s:
        #     if i in only:
        #         only.remove(i)
        #         if not(i in overlap):
        #             overlap.append(i)
        #     else:
        #         if not(i in overlap):
        #             only.append(i)
        # only.sort()
        # return "".join(only + overlap)

        # result : list = []
        # for i in s:
        #     if i in result:
        #         index = result.index(i)
        #         if index+1 == len(result):
        #             continue
        #         else:
        #             if result[index+1] > i:
        #                 continue
        #             else:
        #                 del result[index]
        #                 result.append(i)            
        #     else:
        #         result.append(i)
        # return ''.join(result)

        counter, seen, stack = collections.Counter(s), set(), []

        for i in s:
            counter[i] -= 1
            if i in seen:
                continue
            while stack and i < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(i)
            seen.add(i)
        return ''.join(stack)
        

s = "cbacdcbc"
# s = "bcabc"
sol = Solution()
print(sol.removeDuplicateLetters(s))                           
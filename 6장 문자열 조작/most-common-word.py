# https://leetcode.com/problems/most-common-word/

# 가장 흔한 단어찾기
# 정규표현식으로 전처리 단어만 남기되 띄어쓰기나 구두점으로 식별


import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:   
        # paragraph = re.sub('[^\w]', ' ', paragraph)   
        # paragraph = paragraph.lower()
        # for i in paragraph.split():
        #     for i in banned:
        #         del paragraph.remove(i)        


        # counters = collections.Counter(paragraph.split())
        # return counters.most_common(1)[0][0]
        words = [word for word in re.sub('[^\w]', ' ', paragraph)
            .lower().split()
                if word not in banned]
                
        counters = collections.Counter(words)
        return counters.most_common(1)[0][0]                
        

        




        
# s = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
s = "abc abc? abcd the jeff!"
banned = ["abc","abcd","jeff"]

sol = Solution()
print(sol.mostCommonWord(s, banned))        
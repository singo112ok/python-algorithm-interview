# https://leetcode.com/problems/valid-palindrome/

# 팰린드롬(회문) 조사 , 앞뒤가 똑같은지 구분
# 영문자와 숫자만 대상이니 정규표현식으로 처리 -> 대소문자 구분안하므로 다 대문자 변경
# -> 리스트 슬라이스를 이용해서 맨앞과 뒤 비교

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = str.upper(re.sub('[^a-zA-Z0-9]','',s))
        for i in range(int(len(s)/2)):
            if s[i] != s[-i-1]:
                return False
        return True                


# s = "A man, a plan, a canal: Panama"
s = "race a car"
sol = Solution()
print(sol.isPalindrome(s))
# https://leetcode.com/problems/reverse-string/

# 문자열을 뒤집어야하는데 리턴없이 리스트 내부를 뒤집기
# 투포인트로 뒤집기 혹은 리스트 뒤집기 함수

class Solution:
    def reverseString(self, s: list[str]) -> None:
        # s[:] = s[::-1]
        # s.reserve()
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
  
        

s = ["h","e","l","l","o"]
sol = Solution()
sol.reverseString(s)
print(s)
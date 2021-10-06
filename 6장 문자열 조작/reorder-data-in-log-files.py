# https://leetcode.com/problems/reorder-data-in-log-files/

# 로그 재정렬하기 
# split으로 나눈 뒤 정렬

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        num_list = []
        temp_list = []

        for log in logs:

            if log.split()[1][0] <= '9' and log.split()[1][0] >= '0':
                num_list.append(log)            
            else:
                temp_list.append(log)
        
        temp_list.sort(key=lambda a:(a.split()[1:], a.split()[0]))

        return temp_list+num_list
        

# s = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# s = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
s = ["n 1 6", "r wyv", "7 72", "4 95", "x 706"]
sol = Solution()
print(sol.reorderLogFiles(s))

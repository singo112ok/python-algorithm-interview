# https://leetcode.com/problems/group-anagrams/

#딕셔너리를 사용하여 값을 넣고 출력할 줄 아는가

import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ana_str = collections.defaultdict(list)
        for word in strs:
            ana_str[''.join(sorted(word))].append(word)
        return list(ana_str.values())        

        
strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))

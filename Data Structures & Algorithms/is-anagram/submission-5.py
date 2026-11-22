class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkS = sorted(s)
        checkT = sorted(t)
        return checkS == checkT
       
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = list(s), list(t) 
        s1.sort()
        t1.sort()
        if str(s1) == str(t1):
            return True
        return False


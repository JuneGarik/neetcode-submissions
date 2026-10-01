class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = list(s), list(t) 
        s1.sort()
        t1.sort()
        s2 = tuple(s1)
        t2 = tuple(t1)
        if s2 == t2:
            return True
        return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct1 = {}
        dct2 = {}
        for i in s:
            dct1.setdefault(i, 0)
            dct1[i] += 1
        print(dct1)

        dct2 = {}
        for i in t:
            dct2.setdefault(i, 0)
            dct2[i] += 1
        print(dct2)

        if dct1 == dct2:
            return True
        return False


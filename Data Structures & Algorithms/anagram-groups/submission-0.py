class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = {}
        for i, string in enumerate(strs):
            string = "".join(sorted(string))
            if string in seen:
                seen[string] += (i,)
            else:
                seen[string] = (i,)
        
        for args in seen.values():
            list_n = []
            for part in list(args):
                list_n.append(strs[part])
            result.append(list_n)
        
        return result
            

        


        
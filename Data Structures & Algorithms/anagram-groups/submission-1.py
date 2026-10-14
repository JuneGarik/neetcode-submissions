class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            counter = [0] * 26 # под каждую букву нижнего регистра
            for c in s:
                counter[ord(c) - ord("a")] += 1 # делаем маппинг каждого индекса к букве в каунтере, если "а" то это индекс 0
            res[tuple(counter)].append(s)
        return list(res.values())

            

        


        
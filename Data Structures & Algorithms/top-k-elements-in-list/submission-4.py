class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} # подсчет для количества повторений конкретных значений 
        freq = [[] for i in range(len(nums) + 1)] # список со вложенным списком, который будет для кол-во повторений присваивать ключ: сами значения

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for n, c in counter.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res





        

        
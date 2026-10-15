class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {} #словарь для сбора всех повторений значений
        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        prep_sort = sorted(dct.items(), key = lambda pair: pair[1], reverse = True) # сделали список из отсортированных кортежей
        result = []
        for i in range(k):
            result.append((prep_sort[i])[0])
        
        return result
            


        

        
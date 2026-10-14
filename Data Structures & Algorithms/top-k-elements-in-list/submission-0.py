class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {} #словарь для сбора всех повторений значений
        for num in nums:
            dct.setdefault(num, 0)
            dct[num] += 1
        
        prep = tuple(dct.items()) # составили кортеж из ключ, значение, (('2',3),('4', 2))
        prep_sort = sorted(prep, key = lambda pair: pair[1], reverse = True) # сделали список из отсортированных кортежей
        result = []
        for i in range(k):
            result.append((prep_sort[i])[0])
        
        return result
            


        

        
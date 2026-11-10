class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [] #находим все произведения начиная с левой части 
        postfix = [] #находим все произведения с провой части
        
        j = 1
        for i in range(len(nums)):
            j *= nums[i]
            prefix.append(j)
        
        k=1
        for i in range(len(nums)-1, -1, -1):
            k *= nums[i]
            postfix.append(k)
        postfix.reverse()

        for i in range(len(nums)):
            if i == 0:
                nums[i] = postfix[i+1]
            elif i == (len(nums) - 1):
                nums[i] = prefix[len(nums)-2]
            else:
                nums[i] = prefix[i-1] * postfix[i+1]
        
        return nums
            
        

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevhashMap = {}
        for i,num in enumerate(nums): 
            other = target - num
            if other in prevhashMap:
                return [prevhashMap[other],i]
            prevhashMap[num] = i
  
        

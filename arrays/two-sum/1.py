def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashMap = {}
    for i, num in enumerate(nums):
        hashMap[num] = i

    for i, num in enumerate(nums):
        other = target - num
        if other in hashMap and hashMap[other] != i:
            return [i, hashMap[other]]

        

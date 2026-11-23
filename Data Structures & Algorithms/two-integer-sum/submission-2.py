class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt: [int,int] = {}
        for i, num in enumerate(nums):
            if (target - num) in dictt:
                return [dictt[target - num], i]
            else:
                dictt[num] = i
        return []
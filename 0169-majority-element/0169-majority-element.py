class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, c = -1, 0

        for i in nums:
            if c == 0: res = i
            if i == res: c += 1
            else: c -= 1
        
        return res
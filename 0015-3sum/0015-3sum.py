class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            v = nums[i]
            a, b = i + 1, len(nums) - 1

            if i > 0 and v == nums[i - 1]: continue

            while a < b:
                s = v + nums[a] + nums[b]
                if s > 0: b -= 1
                elif s < 0: a += 1
                else:
                    res.append([v, nums[a], nums[b]])
                    a += 1
                    b -= 1


                    while b > a and nums[a - 1] == nums[a]: a += 1
                    #while nums[b + 1] == nums[b] and b > a: b -= 1
        
        return res

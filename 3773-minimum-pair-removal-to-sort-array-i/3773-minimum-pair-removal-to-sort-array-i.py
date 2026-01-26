class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0

        while True:
            print(nums)
            min_sum, pair_pos = 50001, 0
            #print(min_sum, pair_pos)

            idx = 0
            while idx < len(nums) - 1:
                if nums[idx + 1] < nums[idx]:
                    break
                idx += 1
            #print(idx, len(nums))
            if idx == len(nums) - 1:
                return res

            for i in range(0, len(nums) - 1):
                if nums[i] + nums[i + 1] < min_sum:
                    pair_pos = i
                    min_sum = nums[i] + nums[i + 1]

            #print(pair_pos)
            nums.pop(pair_pos + 1)
            nums[pair_pos] = min_sum

            res += 1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a, b = 0, len(numbers) - 1

        while a < b:
            current_sum = numbers[a] + numbers[b]
            if current_sum == target: return [a + 1, b + 1]
            elif current_sum < target: a += 1
            else: b -= 1

        return [-1, -1] 
        
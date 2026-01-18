class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(1, len(strs)):
            j, l = 0, min(len(res), len(strs[i]))

            while j != l and res[j] == strs[i][j]:
                j += 1
            
            if len(res) > j:
                res = res[:j]
        
        return res

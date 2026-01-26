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

    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(len(strs) - 1):
            temp_res = ""
            str1, str2 = strs[i], strs[i + 1]
            if len(str1) > len(str2):
                str1, str2 = str2, str1

            for j in range(len(str1)):
                if str1[j] == str2[j]:
                    temp_res += str1[j]
                else:
                    break
            
            if len(temp_res) < len(res):
                res = temp_res
        
        return res
    """
            
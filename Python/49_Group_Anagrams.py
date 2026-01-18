class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # make unordered dict
        for s in strs:
            char_counts = [0] * 26
            for c in s:
                char_counts[ord(c) - 97] += 1
            
            key = tuple(char_counts)

            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        
        return list(res.values())
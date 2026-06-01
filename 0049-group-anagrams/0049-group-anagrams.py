class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res, gr = [], defaultdict(list)
        print(self.get_anagram("bobby"))

        for s in strs:
            gr[self.get_anagram(s)].append(s)
        
        res.extend(gr.values())
        return res
    

    def get_anagram(self, s) -> int:
        co = [0] * 26
        for c in s:
            #            a
            co[ord(c) - 97] += 1

        res = []
        for i in range(26):
            if co[i] != 0:
                res.extend([chr(i + 97), str(co[i])])
        
        return "".join(res)
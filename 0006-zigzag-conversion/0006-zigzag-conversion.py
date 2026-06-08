class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1: return s

        i, d, r = 0, 1, [""] * numRows
        print(r)
        
        for c in s:
            r[i] += c
            if i == 0: d = 1
            elif i == numRows - 1: d = -1
            i += d
        
        #for i in range(numRows): r[i] = "".join(r[i])
        print(r)
        return "".join(r)
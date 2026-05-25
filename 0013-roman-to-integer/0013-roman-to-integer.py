class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        #print(list(zip(s, s[1:])))

        for i in range(len(s) - 1):
            a = s[i]
            b = s[i + 1]
            if vals[a] < vals[b]: 
                res -= vals[a]
            else: 
                res += vals[a]
        
        return res + vals[s[-1]]
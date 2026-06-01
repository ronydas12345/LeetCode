class Solution:
    def reverseWords(self, s: str) -> str:
        #return " ".join(s.split()[::-1])

        res, N, i = [], len(s), 0
        while i < N:
            while i < N and s[i] == " ": i += 1
            if i >= N: break

            j = i
            while j < N and s[j] != " ": j += 1

            w = ""
            for k in range(i, j):
                w += s[k]
            
            res.append(w)
            i = j

        fin, M = "", len(res)
        
        for k in range(M - 1, -1, -1):
            fin += res[k]
            if k > 0: fin += " "
        
        return fin
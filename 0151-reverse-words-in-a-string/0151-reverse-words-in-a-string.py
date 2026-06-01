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
    
        a, b = 0, len(res) - 1
        while a < b:
            res[a], res[b] = res[b], res[a]
            a, b = a + 1, b - 1

        fin = ""
        for k in range(len(res)):
            fin += res[k]
            if k < len(res) - 1:
                fin += " "
        
        return fin
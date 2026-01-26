class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq = {}
        for w in words:
            freq[w] = words.count(w)
        
        print(freq)
        
        M = len(words[0])
        N = M * len(words)
        res = []
        for char in range(M):
            l = char
            curr = {}
            window = 0
            for r in range(char, len(s), M):
                r_word = s[r : r + M]
                if r_word in freq:
                    if r_word in curr:
                        curr[r_word] += 1
                    else:
                        curr[r_word] = 1

                    if curr[r_word] <= freq[r_word]:
                        window += 1

                    print("before:", window)
                    while curr[r_word] > freq[r_word]:
                        l_word = s[l : l + M]
                        curr[l_word] -= 1
                        #if curr[l_word] == 0:
                        #    del curr[l_word]
                        l += M

                        if curr[l_word] < freq[l_word]:

                            window -= 1
                    
                    if window == len(words):
                        res.append(l)

                    print("after:", window)
                else:
                    l = r + M
                    curr.clear()
                    window = 0
            
        return res
                        
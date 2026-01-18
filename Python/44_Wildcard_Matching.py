class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # join * in a row
        p_ = []
        for ch in p:
            if ch == '*' and p_ and p_[-1] == '*':
                continue
            p_.append(ch)
        p = ''.join(p_)

        i = 0
        j = 0
        star = -1      # recent pos of *
        match_i = 0    # pos in s for last '*'

        while i < len(s):
            # alpha or '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i, j = i + 1, j + 1

            # record '*' and try match 0 chars first
            elif j < len(p) and p[j] == '*':
                star = j
                match_i = i
                j += 1

            # mismatch w previous '*', expand 1 char
            elif star != -1:
                j = star + 1
                match_i += 1
                i = match_i

            # mismatch with no '*'
            else:
                return False

        # rem '*' in p
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)

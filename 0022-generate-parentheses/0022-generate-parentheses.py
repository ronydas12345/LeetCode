class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        def rec(c, opened, closed, res):
            if opened == n and closed == n:
                res.append("".join(c))
                return
            
            if opened < n:
                c.append("(")
                rec(c, opened + 1, closed, res)
                c.pop()
            
            if closed < opened:
                c.append(")")
                rec(c, opened, closed + 1, res)
                c.pop()
        
        res = []
        rec([], 0, 0, res)
        return res

    """def generateParenthesis(self, n: int) -> list[str]:
        res, q = [], [("", 0, 0)]

        while q:
            c, opened, closed = q.pop(0)

            if len(c) >= 2 * n:
                res.append(c)
                continue
            
            if opened < n:
                q.append((c + "(", opened + 1, closed))
            
            if closed < opened:
                q.append((c + ")", opened, closed + 1))
        
        return res"""




    
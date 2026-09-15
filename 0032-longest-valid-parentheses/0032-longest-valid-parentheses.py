class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st, res = [-1], 0

        for i, char in enumerate(s):
            if char == "(":
                st.append(i)
            else:
                st.pop()

                if not st: st.append(i)
                else:
                    res = max(res, i - st[-1])
        
        return res

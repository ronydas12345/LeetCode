class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        N = len(s)

        pref_sum   = [0] * (N + 1)
        pref_x     = [0] * (N + 1)
        pref_count = [0] * (N + 1)
        power      = [1] * (N + 1)

        for i in range(1, N + 1):
            power[i] = (power[i-1] * 10) % MOD

        for i in range(1, N + 1):
            d = int(s[i-1])
            pref_sum[i] = pref_sum[i-1] + d

            if d == 0:
                pref_x[i]     = pref_x[i-1]
                pref_count[i] = pref_count[i-1]
            else:
                pref_x[i]     = (pref_x[i-1] * 10 + d) % MOD
                pref_count[i] = pref_count[i-1] + 1

        res = []
        for a, b in queries:
            a += 1
            b += 1

            dig_sum = pref_sum[b] - pref_sum[a-1]

            nonzeros_cnt = pref_count[b] - pref_count[a-1]

            x = (
                pref_x[b]
                - pref_x[a-1] * power[nonzeros_cnt]
            ) % MOD

            res.append((x * dig_sum) % MOD)

        return res

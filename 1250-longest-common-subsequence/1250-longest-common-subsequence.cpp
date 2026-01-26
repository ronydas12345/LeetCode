#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size();
        int m = text2.size();

        int** dp = (int**) calloc(sizeof(int*), n + 1);
        for (int i = 0; i <= n; i ++) {
            dp[i] = (int*) calloc(sizeof(int), m + 1);
        }

        //int dp[n + 1][m + 1] = {0};

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    if (dp[i - 1][j] > dp[i][j - 1]) {
                        dp[i][j] = dp[i - 1][j];
                    } else {
                        dp[i][j] = dp[i][j - 1];
                    }
                }
            }
        }

        int res = dp[n][m];
        //for (int i = 0; i <= n; i ++) free(dp[i]);
        //free(dp);

        return res;
    }
};

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";

        int start = 0, max_len = 1;

        for (int i = 0; i < s.length(); i++) {
            int l1 = step(s, i, i);
            int l2 = step(s, i, i + 1);

            int curr_len = max(l1, l2);

            if (curr_len > max_len) {
                max_len = curr_len;
                start = i - (max_len - 1) / 2;
            }
        }

        return s.substr(start, max_len);
    }

    int step(string s, int left, int right) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            left--;
            right++;
        }
        return right - left - 1; // length
    }
};

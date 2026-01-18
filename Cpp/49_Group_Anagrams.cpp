class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;

        for (string& s : strs) {
            vector<int> char_counts(26, 0);
            for (char c : s) {
                char_counts[c - 'a']++;
            }

            // convert counts into a string key
            string key;
            for (int count : char_counts) {
                key += to_string(count) + "#"; 
            }

            res[key].push_back(s);
        }

        vector<vector<string>> ans;
        for (auto& pair : res) {
            ans.push_back(move(pair.second));
        }

        return ans;
    }
};
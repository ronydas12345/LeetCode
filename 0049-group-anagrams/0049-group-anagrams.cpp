class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;

        for (int i = 0; i < strs.size(); i++) {
            string s = strs[i];
            vector<int> char_counts(26, 0);

            for (int j = 0; j < s.size(); j++) {
                //cout<<(s[j] - 'a')<<"\n";
                char_counts[s[j] - 'a']++;
            }

            //cout<<char_counts[3]<<"\n";

            string key = "";
            for (int k = 0; k < 26; k++) {
                key += (char_counts[k]);// + "#"; 
            }

            cout<<key<<"\n";
            res[key].push_back(s);
        }

        vector<vector<string>> result;
        for (auto it = res.begin(); it != res.end(); it++) {
            result.push_back(it->second);
        }

        return result;
    }
};
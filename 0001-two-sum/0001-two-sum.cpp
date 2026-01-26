#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> m; int N = nums.size();

        for (int i = 0; i < N; i ++) {
            auto j = m.find(target - nums[i]);
            if (j != m.end()) {
                return {i, j->second};
            }

            m.insert({nums[i], i});
        }

        return {};
    }
};
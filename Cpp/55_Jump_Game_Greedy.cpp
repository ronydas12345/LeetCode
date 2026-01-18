class Solution {
public:
    bool canJump(vector<int>& nums) {
        //7, 5, 4, 3, 2, 1, 0, 4
        int N = nums.size();
        int target_idx = N - 1; 

        for (int i = N - 2; i >= 0; i --) {
            if (nums[i] + i >= target_idx) {
                target_idx = i;
            }
        }
        
        return (target_idx == 0);
    }
};
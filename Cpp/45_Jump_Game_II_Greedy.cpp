class Solution {
public:
    int jump(vector<int>& nums) {
        int N = nums.size();
        if (N <= 1) return 0;

        int start = 1; int end = nums[start - 1];
        int farthest = end; int jumps = 1;

        while (farthest < N - 1) {
            for (int i = start; i <= end; i ++) {
                if (farthest < nums[i] + i) farthest = i + nums[i];
            }

            start = end + 1;
            end = farthest;

            jumps ++;
        }

        return (jumps);
    }
};
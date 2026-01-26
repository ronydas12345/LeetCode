class Solution {
public:
    int maxArea(vector<int>& height) {
        int N = height.size(); int a = 0; int b = N - 1; int res = 0;

        while (a < b) {
            int area = min(height[a], height[b]) * (b - a);
            res = max(area, res);

            if (height[a] < height[b]) {
                a ++;
            } else {
                b --;
            }
        }

        return (res);
    }
};
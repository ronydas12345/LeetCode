class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        vector<int> q; // queue -> vector
        q.push_back(0);

        vector<int> dist(n, -1);
        dist[0] = 0;

        int front = 0;

        while (front < (int) q.size()) {
            int i = q[front++];
            int reach = min(n - 1, i + nums[i]);

            for (int j = i + 1; j <= reach; j++) {
                if (dist[j] == -1) {
                    dist[j] = dist[i] + 1;
                    q.push_back(j);
                    if (j == n - 1) {return dist[j];}
                }
            }
        }
        return -1;
    }
};
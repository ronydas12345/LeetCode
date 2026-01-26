class Solution {
public:
    long long minimumFuelCost(vector<vector<int>>& roads, int seats) {
        int n = roads.size() + 1; // cities
        vector<vector<int>> adj (n);

        for (auto road = roads.begin(); road != roads.end(); road ++) {
            //cout<<road[0][0];
            adj[road[0][0]].push_back(road[0][1]);
            adj[road[0][1]].push_back(road[0][0]);
        }
        
        long long total = 0;
        //long long *arr = dfs(0, -1, adj, seats, &total);
        dfs(0, -1, adj, seats, &total);
        //total += dfs(0, -1, adj, seats, total);
        //total = arr[1];
        return (total); 
    }
    
    int dfs(int node, int parent, vector<vector<int>>& adj, int seats, long long* total) {
        int people = 1;
        for (int i = 0; i < adj[node].size(); i ++) {
            cout<<parent<<" -> "<<node<<", ";
            

            if (adj[node][i] != parent) {
                //long long *arr = dfs(adj[node][i], node, adj, seats, total);
                people += dfs(adj[node][i], node, adj, seats, total);
                //cout<<"\n"<<arr[0]<<" "<<arr[1]<<", ";
                //people += arr[0];
                //total += arr[1];
            }
        }

        if (node != 0) {
            long long cars = (people + seats - 1) / seats;
            (*total) += 1 /* liters per road = 1*/ * cars;
        }

        //long long arr2[2] = {people, total};
        return people;
    }
};
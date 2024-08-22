#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class solution {
public:
    vector<int> shortestPath(vector<vector<int>>& edges, int n, int m, int src) {
        vector<int> adj[n];

        for (int i = 0; i < m; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        queue<int> q;
        vector<bool> visited(n, false);
        vector<int> ans(n, -1);  // Initialize with -1 to indicate unvisited nodes

        q.push(src);
        visited[src] = true;
        ans[src] = 0;

        while (!q.empty()) {
            int val = q.front();
            q.pop();
            for (auto x : adj[val]) {
                if (!visited[x]) {
                    visited[x] = true;
                    q.push(x);
                    ans[x] = ans[val] + 1;
                }
            }
        }
        return ans;
    }
};

int main() {
    int n = 9;
    int m = 10;
    vector<vector<int>> edges = {{0, 1}, {0, 3}, {3, 4}, {4, 5}, {5, 6}, {1, 2}, {2, 6}, {6, 7}, {7, 8}, {6, 8}};

    solution sol;
    vector<int> result = sol.shortestPath(edges, n, m, 0);

    for (int i = 0; i < n; i++) {
        cout << "Shortest path from 0 to " << i << " is " << result[i] << endl;
    }

    return 0;
}

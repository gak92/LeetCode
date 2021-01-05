class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        
        int m = obstacleGrid.size();
        if(m==0) return 0;
        int n = obstacleGrid[0].size();
        
        vector<vector<int>> dp(m,vector<int>(n,0)); // create dp and fill with 0
        
        for(int i=0; i<m; i++){             // update 1 in first row until find obstacle
            if(obstacleGrid[i][0]==1)
                break;
            dp[i][0] = 1;
        }
        
        for(int i=0; i<n; i++){             // update 1 in first column until find obstacle
            if(obstacleGrid[0][i]==1)
                break;
            dp[0][i] = 1;
        }
        
        for(int i=1; i<m; i++){
            for(int j=1; j<n; j++){
                if(obstacleGrid[i][j]==1)   // if found obstacle then skip it
                    continue;
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        return dp[m-1][n-1];
    }
};
​
​
​
​
​
​
​
​
/*
​
class Solution {
    vector<vector<int>> dp;
    vector<vector<int>> gGrid;
public:
    Solution(): dp(101, vector<int>(101,-1)){}

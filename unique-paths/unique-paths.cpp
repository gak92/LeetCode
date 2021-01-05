class Solution {
    vector<vector<int>> dp;
public:
    Solution(): dp(101, vector<int>(101,-1)){}
    
    int uniquePaths(int m, int n) {
        if(m<1 || n<1)          // check out of bound
            return 0;
        if(m==1 && n==1)        // check first row and first column
            return 1;
        
        if(dp[m][n] != -1)      // if already calculated
            return dp[m][n];  
        
        dp[m][n] = uniquePaths(m,n-1)+uniquePaths(m-1,n);
        
        return dp[m][n];
    }
};
​
​
​
​
// class Solution {
// public:
//     int uniquePaths(int m, int n) {
//         vector<vector<int>> dp(m, vector<int>(n,1)); //initialize with 1
        
//         for(int i=1; i<m; i++){
//             for(int j=1; j<n; j++){
//                 dp[i][j] = dp[i-1][j] + dp[i][j-1];
                
//             }
//         }
        
//         return dp[m-1][n-1];
//     }
// };
​
​
​

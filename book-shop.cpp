#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define f(i,m,n) for(ll i = m; i < n; ++i)
#define rf(i, n, m) for(ll i = n; i >= m; --i)
#define vll vector<long long>





int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x; cin >> n >> x;
    vector<int> prices(n), pages(n);
    f(i, 0, n) cin >> prices[i];
    f(i, 0, n) cin >> pages[i];
    vector<vector<int>> dp(n+1, vector<int>(x+1));
    f(i, 1, n+1) {
        f(m, 1, x+1) {
            dp[i][m] = dp[i-1][m];
            if(m >= prices[i-1]) dp[i][m] = max(dp[i-1][m], pages[i-1] + dp[i-1][m-prices[i-1]]);
        }
    }
    cout << dp[n][x] << "\n";
}
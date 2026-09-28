#include <bits/stdc++.h>
using namespace std;
using ll = long long;
 
#define f(i,m,n) for(ll i = m; i < n; ++i)
ll MOD = 1000000007;
 
void solve() {
    ll a, b;
    cin >> a >> b;
    
    ll res = 1;
    ll base = a % MOD;
    
 
    if (b == 0) {
        cout << 1 << endl;
        return;
    } else if (a == 0) {
        cout << 0 << endl;
        return;
    }
 
 
    while (b>0) {
        if (b%2!=0) {
            res = (res*base) % MOD;
        }
        
        base = (base*base) % MOD;
        b/=2;
    }
 
    cout << res << endl;
}
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
 
    int n; cin >> n;
    while (n--) solve();
}

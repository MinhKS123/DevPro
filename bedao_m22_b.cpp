#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define f(i,m,n) for(ll i = m; i < n; ++i)
#define vll vector<long long>

void solve() {
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ll n; cin >> n;
    vll list_n;
    int cnt[23] = {0};
    ll ans = 0;
    f(_, 0, n) {
        ll temp; cin >> temp;
        list_n.push_back(temp);
    }
    
    f(j, 6, n) {
        cnt[list_n[j-6]%23]++;
        ans+=cnt[(list_n[j]%23+23)%23];
    }
    cout << ans << endl;
}

#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define f(i,m,n) for(ll i = m; i < n; ++i)
#define rf(i, n, m) for(ll i = n; i >= m; --i)
#define vll vector<long long>





int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n;
    int total = 1 << n;
    f(i, 0, total) {
        int gray = i ^ (i >> 1);
        string s = bitset<16>(gray).to_string().substr(16-n);
        cout << s << '\n';
    }
}
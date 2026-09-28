#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define f(i,m,n) for(ll i = m; i < n; ++i)
#define rf(i, n, m) for(ll i = n; i >= m; --i)
#define vll vector<long long>

vll weights;
int n;
ll total = 0;

ll solve(ll sumA, int index) {
    ll sumB = 0;
    if (index == n) {
        sumB = total - sumA;
        return abs(sumA - sumB);
    }

    ll A = solve(sumA + weights[index], index + 1);
    ll B = solve(sumA, index + 1);
    return min(A, B);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    weights.resize(n);
    f(i, 0, n) {
        cin >> weights[i];
        total += weights[i];
    }
    ll ans = solve(0, 0);
    cout << ans << endl;
}
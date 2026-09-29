#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define f(i,m,n) for(ll i = m; i < n; ++i)
#define rf(i, n, m) for(ll i = n; i >= m; --i)
#define vll vector<long long>

unordered_map<char, int> freq;
int l = 0;
string str;
string result;
vector<string> res;

ll fact(ll n) {
    ll res = 1;
    f(i, 1, n+1) {
        res*=i;
    }
    return res;
}

void solve() {
    // base case goes here
    if (result.size() == l) {
        res.push_back(result);
        return;
    }

    //backtrack
    for (char c = 'a'; c <= 'z'; ++c) {
        if (freq[c] > 0) {
            result.push_back(c);
            freq[c]--;

            solve();

            freq[c]++;
            result.pop_back();
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> str;
    l = str.size();
    ll k = 1;
    for (auto const& i : str) {
        freq[i]++;
        k *= freq[i];
    }
    k = fact(l)/k;
    cout << k << endl;
    solve();
    for (auto const& str : res) {
        cout << str << endl;
    }
}
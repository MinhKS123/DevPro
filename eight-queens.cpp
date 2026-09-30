#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define f(i,m,n) for(ll i = m; i < n; ++i)
#define rf(i, n, m) for(ll i = n; i >= m; --i)
#define vll vector<long long>

vector<pair<int, int>> cors;
vector<vector<char>> B(8, vector<char>(8));
int res = 0;
int row = 0;

void backtrack() {
    if (cors.size() == 8) {
        res++;
        return;
    }
    
    f(col, 0, 8) {
        if (B[row][col] == '*') continue;

        bool ok = true;
        for(auto const& cor : cors) {
            if (cor.second == col) {ok = false; break;}
            if ((cor.second - cor.first) == (col - row)) {ok = false; break;}
            if ((cor.first + cor.second) == (col + row)) {ok = false; break;}
        }

        if(ok) {
            cors.push_back({row,col});
            row++;
            backtrack();
            row--;
            cors.pop_back();
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    f(i, 0, 8) {
        f(j, 0, 8) cin >> B[i][j];
    }
    backtrack();
    cout << res << endl;
}
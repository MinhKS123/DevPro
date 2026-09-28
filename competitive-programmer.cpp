#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define f(i,m,n) for(ll i = m; i < n; ++i)
#define rf(i, n, m) for(ll i = n; i >= m; --i)
#define vll vector<long long>

void solve() {
    string str_num;
    cin >> str_num;
    int l = str_num.size();
    vector<int> digits;
    rf(i, l - 1, 0) {
        digits.push_back(str_num[i] - '0');
    }
    int sum = accumulate(digits.begin(), digits.end(), 0);
    if (sum % 3 != 0) {
        cout << "cyan" << endl;
        return;
    } 
    bool flag = false;
    for (auto digit : digits) {
        if (digit==0) {
            flag = true;
            break;
        }
    }
    if (flag == false) {
        cout << "cyan" << endl;
        return;
    } else {
        int count_even = 0;
        for (auto digit : digits) {
            if (digit%2==0) {
                ++count_even;
            }
        }
        if (count_even >= 2) {
            cout << "red" << endl;
            return;
        } else {
            cout << "cyan" << endl;
            return;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n;
    while(n--) solve();
}

#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll n, m;
    cin >> n >> m;
    cout << n * (n - 1) / 2 + m * (m - 1) / 2 << '\n';
    return 0;
}

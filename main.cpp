#include <bits/stdc++.h>


using namespace std;



vector<int> primeFactors(int n){
	vector<int> factors;

	while (n%2==0){
		factors.push_back(2);
		n/=2;
	}
	for (int i =3; i*i <=n;i=i+2){
		while (n%i ==0){
			factors.push_back(i);
			n/=i;
		}
	}
	if (n>2){
		factors.push_back(n);
	}
	return factors;
}

vector<int> simplify(vector<int> n){
	set<int> b(n.begin(), n.end());
	n.clear();
	n.assign(b.begin(), b.end());
	return n;
}


bool check(int a, int b){
	vector<int> a_vec = simplify(primeFactors(a));
	vector<int> b_vec = simplify(primeFactors(b));
	return (a_vec == b_vec);
}
	
int main(){
	int n, k;
	cin >> n >> k;
	cin.ignore();
	string input;
	getline(cin, input);
	istringstream iss(input);
	vector<int> array;
	int c;
	while (iss >> c){
		array.push_back(c);
	}
	vector<int> ans;
	for (int ele : array){
		if (check(ele, k)){
			ans.push_back(ele);
		}
	}
	ans = simplify(ans);
	cout << ans.size() << endl;
	for (int ele_out : ans){
		cout << ele_out << " ";
	}
	return 0;
}


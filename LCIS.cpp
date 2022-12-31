#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
   int findLengthOfLCIS(vector<int>& nums) {
      if (nums.size() <= 1)
         return nums.size();
      int answer = 1, count = 1;
      for (int i = 0; i < nums.size() - 1; i++) {
         if (nums[i] <= nums[i + 1]) {
            count++;
            answer = max(answer, count);
         }
         else {
            count = 1;
         }
      }
      return answer;
   }
};

int main(){
    int n;
    cin >> n;
    int input;
    vector<int> arr;
    for (int i = 0; i < n; ++i){
        cin >> input;
        arr.push_back(input);
    }
    Solution ob;
    cout << (ob.findLengthOfLCIS(arr));
}
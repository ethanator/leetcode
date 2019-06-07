#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  int fixedPoint(vector<int>& A) {
    for (int i = 0; i < A.size(); i++) {
      if (A[i] == i) return i;
    }
    return -1;
  }
};

int main() {
  Solution sol;
  vector<int> input1 = {-10, -5, 0, 3,  7};
  vector<int> input2 = {  0,  2, 5, 8, 17};
  vector<int> input3 = {-10, -5, 3, 4,  7, 9};

  cout << sol.fixedPoint(input1) << endl;
  cout << sol.fixedPoint(input2) << endl;
  cout << sol.fixedPoint(input3) << endl;
}
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

class Solution {
public:
  int trap(vector<int>& height) {
    int left = 0, right = height.size() - 1, leftMax = 0, rightMax = 0, area = 0;
    while (left < right) {
      if (height[left] < height[right]) {
        if (height[left] > leftMax) {
          leftMax = height[left];
        } else {
          area += leftMax - height[left];
        }
        left++;
      } else {
        if (height[right] > rightMax) {
          rightMax = height[right];
        } else {
          area += rightMax - height[right];
        }
        right--;
      }
    }
    return area;
  }
};

int main() {
  vector<int> elevations{0, 5, 2, 1, 2, 1, 5, 0, 0};
  Solution sol;
  cout << sol.trap(elevations) << endl;
}

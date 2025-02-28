# **Lab 05: Solving the Trapping Rain Water Problem**

In this lab, you will explore different approaches to solving the **Trapping Rain Water** problem. This problem is a classic algorithmic challenge that demonstrates the importance of preprocessing and efficient traversal techniques.

## **Problem Statement**
Given an array **arr[]** representing the height of bars in a histogram where the width of each bar is **1**, compute how much water can be trapped after rain.

### **Example**

#### **Input:**
```
arr[] = {2, 1, 5, 3, 1, 0, 4}
```
#### **Output:**
```
9
```

```
Height Representation:
      
      #
      #           #
      #  #        #
#     #  #        #
#  #  #  #  #     #
-------------------
2  1  5  3  1  0  4

Trapped Water:
  
      #
      #  W  W  W  #
      #  #  W  W  #
#  W  #  #  W  W  #
#  #  #  #  #  W  #
-------------------
2  1  5  3  1  0  4

Total Trapped Water = 9 units
```

---

## **Objectives**
By the end of this lab, you should:
1. Understand the Trapping Rain Water problem and its importance.
2. Understand a **Brute Force** approach with O(n^2) time complexity.
3. Develop an **Optimized Prefix-Suffix** approach with O(n) time complexity and O(n) space complexity.
4. Implement an **Optimal Two-Pointer** approach with O(n) time and O(1) space.
5. (Bonus) Think about how to solve the problem using **Stacks**.

---

## **Approach 1: Brute Force (Exhaustive Search)**

### **Explanation**
For each index **i**, find the maximum bar height to its **left** and the maximum bar height to its **right**. The amount of water that can be trapped at index **i** is given by:

\[ \text{water}[i] = \min(\text{leftMax}, \text{rightMax}) - \text{arr}[i] \]

Iterate over all indices and sum up the trapped water.

### **Pseudocode**
```
1. Initialize result = 0
2. Loop i from 1 to n-2 (since first and last elements cannot trap water):
    a. Find max height to the left of i (leftMax)
    b. Find max height to the right of i (rightMax)
    c. Calculate water[i] = min(leftMax, rightMax) - arr[i]
    d. If water[i] is positive, add it to result
3. Return result
```

### **C++ Implementation**
```cpp
#include <iostream>
#include <vector>
using namespace std;

int maxWater(vector<int>& arr) {
    int res = 0;
    for (int i = 1; i < arr.size() - 1; i++) {
        int leftMax = arr[i];
        for (int j = 0; j < i; j++)
            leftMax = max(leftMax, arr[j]);

        int rightMax = arr[i];
        for (int j = i + 1; j < arr.size(); j++)
            rightMax = max(rightMax, arr[j]);

        res += max(0, min(leftMax, rightMax) - arr[i]);
    }
    return res;
}

int main() {
    vector<int> arr = {2, 1, 5, 3, 1, 0, 4};
    cout << maxWater(arr) << endl;
    return 0;
}
```

---

## **Approach 2: Prefix-Suffix Maximums (Efficient Preprocessing)**

### **Explanation**
Instead of computing left and right max for each element separately, preprocess these values first in two arrays:
- **leftMax[i]** stores the max height from **index 0 to i**.
- **rightMax[i]** stores the max height from **index i to n-1**.

After preprocessing, compute water at each index in **O(1)** time using:
\[ \text{water}[i] = \min(\text{leftMax}[i], \text{rightMax}[i]) - \text{arr}[i] \]

### **Pseudocode**
```
1. Create arrays leftMax[n] and rightMax[n]
2. Compute leftMax: leftMax[i] = max(leftMax[i-1], arr[i])
3. Compute rightMax: rightMax[i] = max(rightMax[i+1], arr[i])
4. Initialize result = 0
5. Loop i from 1 to n-2:
    a. water[i] = min(leftMax[i-1], rightMax[i+1]) - arr[i]
    b. If water[i] is positive, add it to result
6. Return result
```

### **Task**
Implement this approach in **C++** following the above pseudocode.

---

## **Approach 3: Two-Pointer Technique (Optimal Solution)**

### **Explanation**
Use two pointers (**left** and **right**) moving inward. Maintain two variables:
- **lMax**: Maximum height on the left.
- **rMax**: Maximum height on the right.

At each step, process the smaller boundary and move the pointer inward.

### **Pseudocode**
```
1. Initialize left = 1, right = n-2
2. Set lMax = arr[0], rMax = arr[n-1]
3. Initialize result = 0
4. While left <= right:
    a. If rMax <= lMax:
        i. Add max(0, rMax - arr[right]) to result
        ii. Update rMax = max(rMax, arr[right])
        iii. Move right pointer left
    b. Else:
        i. Add max(0, lMax - arr[left]) to result
        ii. Update lMax = max(lMax, arr[left])
        iii. Move left pointer right
5. Return result
```

### **Task**
Implement this approach in **C++** following the above pseudocode.

---

## **Bonus Challenge: Stack-Based Solution**

Can you solve this problem using **Stacks**?
- Consider storing indices in a **monotonic stack**.
- Process elements efficiently by maintaining a decreasing sequence.
- Use **pop operations** when a taller bar is found to compute trapped water.

### **Hints:**
- The stack stores indices of bars.
- When a taller bar appears, compute trapped water for popped bars.
- Use the difference between indices for width calculation.
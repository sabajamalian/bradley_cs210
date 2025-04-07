# **Lab 10: Unique Permutations with Duplicates – Backtracking**

In this lab, you'll practice solving a **backtracking** problem involving permutations of numbers that **may contain duplicates**. The goal is to generate **all unique permutations** of the given list. You’ll write a recursive backtracking solution that carefully avoids generating duplicate results.

---

## **Problem Statement**

Given a list of integers `nums`, which may include **duplicate values**, your task is to return **all possible unique permutations** of the list.

- You **must not** return duplicate permutations.
- The result can be in any order.

### **Example**

#### **Input:**
```
nums = [1, 1, 2]
```

#### **Output:**
```
[
  [1, 1, 2],
  [1, 2, 1],
  [2, 1, 1]
]
```

---

## **Objectives**

By the end of this lab, you should be able to:

1. Understand how backtracking can be used to build permutations.
2. Implement a solution that avoids duplicates using pruning techniques.
3. Apply recursion with state tracking using auxiliary structures like visited arrays.

---

## **Approach**

To solve this problem, we use **backtracking** with the following techniques:

1. **Sort the input list** to make it easier to identify and skip duplicate values.
2. Use a **visited array** to track which elements have been used in the current permutation.
3. In the loop, **skip over duplicates**: if `nums[i] == nums[i-1]` and the previous duplicate wasn't used, skip it.

This avoids generating permutations that are the same due to duplicate values.

---

## **Pseudocode**

```
function permuteUnique(nums):
    sort(nums)
    result = []
    used = [False] * len(nums)

    function backtrack(path):
        if length(path) == length(nums):
            result.append(copy of path)
            return
        for i from 0 to len(nums) - 1:
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result
```

---

## **Function Signature**

You will implement the following function in C++:

```cpp
vector<vector<int>> permuteUnique(vector<int>& nums);
```

---

## **Main Function**

Use this code snippet to test your implementation with different input cases:

```cpp
int main() {
    vector<vector<int>> test_cases = {
        {1, 1, 2},
        {1, 2, 3},
        {2, 2, 1, 1}
    };

    for (auto& nums : test_cases) {
        cout << "Input: ";
        for (int num : nums) cout << num << " ";
        cout << "\nOutput:\n";

        auto result = permuteUnique(nums);
        for (auto& perm : result) {
            cout << "[ ";
            for (int n : perm) cout << n << " ";
            cout << "]\n";
        }
        cout << "\n";
    }

    return 0;
}
```

---

## **Challenge (10% extra credit)**

- Can you rewrite the algorithm **iteratively** (without recursion)?
- What happens if the input size is very large (e.g., 10+ elements with duplicates)? Can you optimize memory or stack usage?
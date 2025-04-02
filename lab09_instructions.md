
# **Lab 09: Longest Common Subsequence – Brute Force vs Dynamic Programming**

In this lab, you'll explore a classic **dynamic programming** problem: finding the **Longest Common Subsequence (LCS)** of two strings. You’ll implement both a **brute force recursive approach** and an **efficient dynamic programming (DP)** solution, comparing their performance in terms of both correctness and execution time.

---

## **Problem Statement**

Given two strings `s1` and `s2`, your task is to find the **Longest Common Subsequence (LCS)**—the longest sequence of characters that appear in both strings **in the same relative order**, but not necessarily consecutively.


- A **subsequence** is a sequence that appears in the same order but not necessarily contiguously.
- **Example:**  
  For `s1 = "AGGTAB"` and `s2 = "GXTXAYB"`, the LCS is `"GTAB"`.

### **Example**

#### **Input:**
```
s1 = "ABCDE"
s2 = "ACEFG"
```

#### **Output:**
```
LCS = "ACE"
```

---

## **Objectives**

By the end of this lab, you should be able to:

1. Understand the concept of subsequences and how they differ from substrings.
2. Apply recursion and dynamic programming to solve LCS.
3. Analyze and compare the performance of brute force vs dynamic programming solutions.


The brute force method explores **all subsequence combinations**, which leads to **exponential time complexity**. Dynamic programming, on the other hand:

- Stores intermediate results in a **2D table**.
- Avoids redundant calculations using **memoization** or tabulation.
- Reduces the complexity from exponential to **polynomial time (O(m × n))**, where `m` and `n` are the lengths of the input strings.

---

## **Approach**

### **Brute Force (Recursive):**

1. Compare characters at the end of the two strings.
2. If they match, include it in the LCS and move both pointers back.
3. If they don't match, recursively try two options:
   - Exclude last character of `s1`.
   - Exclude last character of `s2`.
4. Return the longer of the two results.

---

### **Dynamic Programming:**

1. Create a 2D table `dp[m+1][n+1]` to store lengths of LCS of substrings.
2. Fill the table using bottom-up approach.
3. Use the table to **reconstruct the LCS string** by backtracking from `dp[m][n]`.

---

## **Pseudocode**

### **Brute Force**
```
function lcs_brute(s1, s2, m, n):
    if m == 0 or n == 0:
        return ""
    if s1[m-1] == s2[n-1]:
        return lcs_brute(s1, s2, m-1, n-1) + s1[m-1]
    else:
        lcs1 = lcs_brute(s1, s2, m-1, n)
        lcs2 = lcs_brute(s1, s2, m, n-1)
        return longer of lcs1 and lcs2
```

### **Dynamic Programming**
```
function lcs_dp(s1, s2):
    m = length of s1
    n = length of s2
    dp = 2D array of size (m+1)x(n+1) filled with 0

    for i from 1 to m:
        for j from 1 to n:
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    Backtrack to build LCS string:
    i = m, j = n, result = ""
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            prepend s1[i-1] to result
            i--, j--
        else if dp[i-1][j] > dp[i][j-1]:
            i--
        else:
            j--

    return result
```

---

## **Function Signatures**

You will implement the following functions in C++:

```cpp
string lcs_brute(string s1, string s2, int m, int n);
string lcs_dp(string s1, string s2);
```

---

## **Main Function**

Use this code to test both implementations and compare their performance:

```cpp
int main() {
    vector<pair<string, string>> test_cases = {
        {"ABCD", "ABDC"},
        {"AGGTAB", "GXTXAYB"},
        {"ABCDE", "ACEFG"},
        {"BRADLEY", "BRAVES"}
    };

    for (auto& test : test_cases) {
        string s1 = test.first;
        string s2 = test.second;
        cout << "Strings: \"" << s1 << "\", \"" << s2 << "\":\n";

        auto start_brute = chrono::high_resolution_clock::now();
        string brute_result = lcs_brute(s1, s2, s1.length(), s2.length());
        auto end_brute = chrono::high_resolution_clock::now();
        double brute_time = chrono::duration<double, micro>(end_brute - start_brute).count();

        auto start_dp = chrono::high_resolution_clock::now();
        string dp_result = lcs_dp(s1, s2);
        auto end_dp = chrono::high_resolution_clock::now();
        double dp_time = chrono::duration<double, micro>(end_dp - start_dp).count();

        cout << "Brute Force: \"" << brute_result << "\" (" << brute_time << " us)\n";
        cout << "DP: \"" << dp_result << "\" (" << dp_time << " us)\n\n";
    }

    return 0;
}
```

---

## **Challenge (10% extra credit)**

- Can you further optimize the space complexity of the DP solution to **O(min(m, n))** using rolling arrays?

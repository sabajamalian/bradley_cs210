# **Lab 06: Solving the Stock Span Problem**

In this lab, you will explore different approaches to solving the **Stock Span** problem. This problem is a classic algorithmic challenge that demonstrates the importance of **stacks**, **preprocessing**, and **efficient traversal techniques**.

## **Problem Statement**
Given a list of daily stock prices, calculate the **span** of each day's price. The span of a stock's price on a given day is the maximum number of consecutive days **(including today)** for which the stock price was **less than or equal to** the price on that day.

### **Example**

#### **Input:**
```
prices[] = {100, 80, 60, 70, 60, 75, 85}
```
#### **Output:**
```
[1, 1, 1, 2, 1, 4, 6]
```

```
Price Representation:

Day:     1   2   3   4   5   6   7
Price: 100  80  60  70  60  75  85
Span:    1   1   1   2   1   4   6
```

---

## **Objectives**
By the end of this lab, you should:
1. Understand the **Stock Span** problem and its importance.
2. Implement a **Brute Force** approach with **O(n²)** time complexity.
3. Develop an **Efficient Stack-Based** approach with **O(n)** time complexity.
4. (Bonus) Explore how this problem relates to **Next Greater Element (NGE)**.

---

## **Approach 1: Brute Force (Naïve Method)**

### **Explanation**
For each day's stock price, check how many consecutive previous days had a lower or equal price.

### **Pseudocode**
```
1. Initialize an array span[] of size n with all values set to 1.
2. Loop i from 0 to n-1:
    a. Loop j from i-1 down to 0 while prices[j] <= prices[i]:
        i. Increment span[i] by 1.
3. Return span[] array.
```

### **C++ Implementation**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> stockSpan(vector<int>& prices) {
    // TODO: implement code here
}

int main() {
    vector<int> prices = {100, 80, 60, 70, 60, 75, 85};
    vector<int> result = stockSpan(prices);

    for (int s : result) {
        cout << s << " ";
    }
    cout << endl;
    return 0;
}
```

---

## **Approach 2: Stack-Based Efficient Solution**

### **Explanation**
- Use a **monotonic stack** to efficiently compute spans.
- The stack stores indices of stock prices in **decreasing order**.
- While a higher price is encountered, pop stack elements and compute the span.

Before reading the pseudocode, try to think about how a Stack data structure can help with introducing a level of pre-processing.

### **Pseudocode**
```
1. Initialize an empty stack.
2. Initialize an array span[] of size n.
3. Loop i from 0 to n-1:
    a. While stack is not empty and prices[stack.top()] <= prices[i], pop stack.
    b. If stack is empty, span[i] = i + 1 (all previous prices were smaller).
    c. Else, span[i] = i - stack.top() (distance to last higher price).
    d. Push index i onto the stack.
4. Return span[] array.
```

### **Task**
Implement this approach in **C++** following the above pseudocode.

---

## **Bonus Challenge: Next Greater Element (NGE) Relation**

The **Stock Span** problem is closely related to the **Next Greater Element** problem:
- In **NGE**, we find the next greater element **to the right** for each element.
- In **Stock Span**, we find the closest greater element **to the left**.
- Both problems can be solved efficiently using **stacks**.

### **Challenge**
Can you modify the **Stock Span** solution to solve **NGE** efficiently?
- Implement **NGE** using **monotonic stacks**.
- Compare both problems and discuss similarities.

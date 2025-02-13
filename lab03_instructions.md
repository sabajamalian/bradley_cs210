# **Lab 03: Implementing a Stack with Different Growth Strategies**

In this lab, you will implement a **Stack** data structure from scratch in C++. You will explore the behavior of a stack using different memory growth strategies:
- **Multiplicative Growth** (e.g., the array size doubles when full)
- **Additive Growth** (e.g., the array size increases by a fixed amount when full)

Stacks are fundamental in programming and are used in recursion, parsing expressions, and managing function calls. It's an important concept in Computer Sciecnce in general and later on during the course we will explore algorithms that would rely on Stack as a data structure to help with optimal and efficient implementations. 

---

## **Objectives**
By the end of this lab, you should:
1. Understand how a **Stack** works.
2. Implement **push, pop, peek, and isEmpty** methods.
3. Handle dynamic array resizing for stack growth.
4. Compare **multiplicative** and **additive** growth strategies.

---

## **Part 1: Understanding Stacks**
A **Stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. This means that the last element added to the stack is the first one to be removed. 
When thinking about Stack operations, consider a stack of plates. When you put the plates away you often stack them on top of the other and when you want to take a plate, you take the one from the top of the stack. Said differently, you wouldn't be able to pull the plate from the middele of the plates stack safely unless you pull all the ones from the top first. So, Last In, First Out. 

### **Stack Operations**
| Operation   | Description |
|------------|-------------|
| **Push(x)** | Adds an element `x` to the top of the stack. |
| **Pop()**   | Removes and returns the top element of the stack. |
| **Peek()**  | Returns the top element without removing it. |
| **isEmpty()** | Checks if the stack is empty. |

Here is an example. In this example we are putting the stack in a linear line from left to the right. This means that bottom of the stack would be the left side and the top of the stack is the right side. 
```
Initial Stack:   [Bottom] 5 → 10 → 15 [Top]
Push(20):        [Bottom] 5 → 10 → 15 → 20 [Top]
Pop(): Returns 20, Stack is now [Bottom] 5 → 10 → 15 [Top]
Peek(): Returns 15, Stack remains unchanged.
```

Here is a YouTube video where YK gives a pretty solid overview of the Stack data structure while comparing it with Queue. It's actually a good YouTube channel to follow if you're interested. Remember how Queue followed a FIFO pattern and now Stack is actually LIFO? 
https://youtu.be/A3ZUpyrnCbM


Furthermore, here is a nice visualization of Push and Pop operatins in Stack by the University of San Francisco: 
https://www.cs.usfca.edu/~galles/visualization/SimpleStack.html

---

## **Part 2: Implementing a Basic Stack in C++**
Your first task is to implement a **basic stack using an array**.

### **Step 1: Define the Stack Class**
- Use an **array** to store elements.
- Keep track of the **top index**.

```cpp
#include <iostream>
using namespace std;

class Stack {
private:
    int* stack;
    int top;
    int capacity;

public:
    Stack(int size = 4) {  // Can you think of why we chose 4 as the starting size? Do you have a better suggestion? 
        stack = new int[size];
        capacity = size;
        top = -1;
    }

    ~Stack() {
        delete[] stack;
    }

    void push(int item) {
        if (top + 1 == capacity) {
            cout << "Stack Overflow" << endl; // This is where stackoverflow.com name come from
            return;
        }
        stack[++top] = item;
    }

    int pop() {
        // Implement your code 
    }

    int peek() {
        // Implement your code
    }

    bool isEmpty() {
        return top == -1;
    }
};
```

### **Step 2: Test Your Stack Implementation**
```cpp
int main() {
    Stack s;
    s.push(10);
    s.push(20);
    cout << s.pop() << endl;  // Output: 20
    cout << s.peek() << endl; // Output: 10
    cout << s.isEmpty() << endl; // Output: 0 (false)
    return 0;
}
```

---

## **Part 3: Implementing Dynamic Stack Growth**
The above stack has a fixed size. Now, we will allow it to expand dynamically.

### **Method 1: Multiplicative Growth (Doubling Size)**
- When the stack is full, **double** its size.

```cpp
void resize(int newCapacity) {
    /*
    To resize a stack, first, create a new array with the desired capacity. Then, 
    copy all existing elements from the old stack into the new array. Once the 
    copying is complete, free the memory occupied by the old array to prevent 
    memory leaks. Finally, update the stack reference to point to the new array 
    and adjust the capacity value accordingly.
    */
}
```

### **Method 2: Additive Growth (Fixed Increase)**
- Instead of doubling, increase by a fixed `c` when full.

```cpp
void resizeAdditive(int increment) {
    // Your implementation
```

---

## **Part 4: Comparing Growth Strategies**
| Strategy   | When Full? | New Size Formula |
|-----------|------------|------------------|
| **Multiplicative Growth** | Double the size | `new_size = 2 * old_size` |
| **Additive Growth** | Increase by `c` | `new_size = old_size + c` |

Compare the two growth strategies based on memory efficiency and performance considerations. Which one is better? Is there a right answer to this question?

### Task
Modify your main function to measure the time taken for a series of push operations. Then save the timing results to a file 
(e.g., stack_timing.csv) so that you generate a graph in Excel to visualize the differences in growth behavior.

Steps to Implement:
- Use the `Timer.h` library available on Canvas to measure the execution time of push operations.
    - You are welcome to implement your own timing functionality too. 
- Run experiments where you push a large number of elements into stacks using:
    - Multiplicative growth (e.g., doubling the capacity).
    - Additive growth (e.g., increasing capacity by a fixed amount).
- Write the timing results to a CSV file, with columns:
    - Number of elements
    - Time taken (in microseconds)
    - Growth strategy used
- Plot the results in Excel, comparing the performance of both strategies.

## **Bonus Challenge**
For **extra credit**, implement:
- A function to **get the current size of the stack**.
- A function to **return the total capacity of the underlying array**.

---


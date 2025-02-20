# **Lab 04: Implementing K-Way Merge Sort**

In this lab, you will implement **K-Way Merge Sort**, an extension of the traditional **Merge Sort** algorithm. This approach divides the array into **K subarrays** instead of just two, recursively sorts them, and then merges them back together efficiently. 

K-Way Merge Sort is an important concept in **divide and conquer** algorithms and has applications in external sorting, large-scale data processing, and optimizing memory access patterns.

Merge Sort is a **divide and conquer** algorithm that splits an array into two halves, sorts each recursively, and then merges the sorted halves.

### **K-Way Merge Sort Approach**
- Instead of dividing into **2 parts**, divide into **K parts**.
- Recursively sort each part using **K-Way Merge Sort**.
- Merge **K sorted parts** back into a single sorted array.

This approach is particularly useful when working with large datasets that do not fit into memory, as it minimizes the number of merge operations.

---

## **Objectives**
By the end of this lab, you should:
1. Understand the standard **Merge Sort** algorithm.
2. Implement **merge_2way**, the standard merge function for two sorted arrays.
3. Extend Merge Sort to a **K-Way Merge Sort**.
4. Analyze performance differences between **2-Way Merge Sort** and **K-Way Merge Sort**.

---

## **Part 1: Implementing a Basic Merge Sort**
Your first task is to implement a standard **2-Way Merge Sort**.

### **Step 1: Implement the Merge Function (`merge_2way`)**
The `merge_2way` function takes a sorted left half and a sorted right half and merges them.

#### **Pseudocode for `merge_2way`**
```
1.  Let size1 = mid - left + 1
    Let size2 = right - mid

2.  Create temporary arrays:
    L of length size1
    R of length size2

3.  For i from 0 to size1-1:
        L[i] = arr[left + i]

    For j from 0 to size2-1:
        R[j] = arr[mid + 1 + j]

4.  Initialize three pointers:
    i = 0  // pointer for L
    j = 0  // pointer for R
    k = left  // pointer for arr, starting at 'left'

5.  While i < size1 AND j < size2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i + 1
        else:
            arr[k] = R[j]
            j = j + 1
        k = k + 1

6.  While i < size1:
        arr[k] = L[i]
        i = i + 1
        k = k + 1

7.  While j < size2:
        arr[k] = R[j]
        j = j + 1
        k = k + 1
```
#### **C++ Implementation**
```cpp
void merge_2way(vector<int>& arr, int left, int mid, int right) {
    int size1 = mid - left + 1;
    int size2 = right - mid;
    // ...
    // TODO: Complete this function using the above pseudocode 
}
```

### **Step 2: Implement 2-Way Merge Sort**
```cpp
// Standard mergesort you've seen before
void mergeSort(vector<int>& arr, int left, int right) {
    if(left < right) {
        int mid = (left + right) / 2;
        // Sort left part
        mergeSort(arr, left, mid);
        // Sort right part
        mergeSort(arr, mid + 1, right);
        // Merge
        merge_2way(arr, left, mid, right);
    }
}
```

---

## **Part 2: Implementing K-Way Merge Sort**
Now, extend Merge Sort to divide into **K** parts instead of just **2**.

### **C++ Implementation of K-Way Merge Sort**

Review the code and understand the difference.

```cpp
// K-WAY MERGE SORT (Basic Approach)
// If subarray size < k, do normal 2-way mergeSort for simplicity.
// Otherwise, determine how many elements per chunk.
// Recursively call kWayMergeSort on each chunk.
// Merge them all in a chain using merge_2way.
void kWayMergeSort(vector<int>& arr, int left, int right, int k) {
    if(left >= right) {
        return; // 0 or 1 element so nothing to sort
    }

    int size = right - left + 1;
    // If fewer elements than k, fallback to 2-way for efficiency purposes
    if(size < k) {
        mergeSort(arr, left, right);
        return;
    }

    // 1) Calculate chunk sizes (with remainder)
    int chunk     = size / k;
    int remainder = size % k;

    // 2) Recursively sort each chunk
    int start = left;
    for(int i = 0; i < k; i++) {
        // If i < remainder, that chunk gets 1 extra element
        int currentChunkSize = chunk;
        if(i < remainder) {
            currentChunkSize++;
        }

        int subLeft  = start;
        int subRight = start + currentChunkSize - 1;

        if(subLeft < subRight) {
            kWayMergeSort(arr, subLeft, subRight, k);
        }

        start = subRight + 1; // move to the next chunk
    }


    // Re-run the same chunking logic to do merges in the same order
    int mergedLeft  = left;
    int firstChunkSize = chunk;
    if(0 < remainder) {
        firstChunkSize++;
    }
    int mergedRight = left + firstChunkSize - 1;

    start = mergedRight + 1;
    for(int i = 1; i < k; i++) {
        int currentChunkSize = chunk;
        if(i < remainder) {
            currentChunkSize++;
        }
        int nextRight = start + currentChunkSize - 1;

        // Merge the results: arr[mergedLeft..mergedRight] with arr[mergedRight+1..nextRight]
        if(mergedRight < nextRight) {
            merge_2way(arr, mergedLeft, mergedRight, nextRight);
            mergedRight = nextRight;
        }
        start = nextRight + 1;
    }
}

void printArray(const vector<int>& arr) {
    for(int x : arr) {
        cout << x << " ";
    }
    cout << endl;
}
```

---

## **Part 3: Comparing 2-Way and K-Way Merge Sort**
You will now compare the performance of **2-Way Merge Sort** and **K-Way Merge Sort**.

### **Task**
1. **Generate random arrays of increasing sizes**.
2. **Sort them using 2-Way Merge Sort and K-Way Merge Sort (k=64)**.
3. **Measure execution time** using `Timer.h` (or your own timing function).
4. **Save results** in a CSV file (`merge_timing.csv`):
   - Number of elements
   - Time taken (microseconds)
   - Sorting method used
5. **Plot the results** in Excel:
   - X-axis: **Number of elements**
   - Y-axis: **Time taken**

The main method to help you get started:
```cpp
int main() {
    srand((unsigned)time(0));

    // Test 1: A small, semi-random array
    vector<int> arr1 = {5, 2, 4, 6, 1, 3};
    cout << "Original arr1: ";
    printArray(arr1);

    mergeSort(arr1, 0, arr1.size() - 1);
    cout << "2-way sorted  : ";
    printArray(arr1);
    cout << endl;

    // Test 2: Already sorted array
    vector<int> arr2 = {1, 2, 3, 4, 5, 6};
    cout << "Original arr2: ";
    printArray(arr2);

    kWayMergeSort(arr2, 0, arr2.size() - 1, 3);
    cout << "3-way sorted  : ";
    printArray(arr2);
    cout << endl;

    // Test 3: Reverse-sorted array
    vector<int> arr3 = {9, 7, 5, 3, 1};
    cout << "Original arr3: ";
    printArray(arr3);

    mergeSort(arr3, 0, arr3.size() - 1);
    cout << "2-way sorted  : ";
    printArray(arr3);
    cout << endl;

    // Test 4: Random array
    vector<int> arr4(100);
    for(int i = 0; i < 100; i++) {
        arr4[i] = rand() % 100; // 0..99
    }
    cout << "Original arr4: ";
    printArray(arr4);

    kWayMergeSort(arr4, 0, arr4.size() - 1, 4);
    cout << "4-way sorted  : ";
    printArray(arr4);
    cout << endl;

    return 0;

    // Pro tips:
    // Create increasingly larger arrays and compare the time of standard merge sort (2-way) vs k-way
    // except choose k to be roughly log(number of elements to sort)
    // the timings will not be indentical but they should be close (the constants matter!)
    // Let's choose k = 64 and compare our k-way merge-soort vs our standard merge sort
    // generate random arrays of increasing size and time both standard mergesort and 64-way mergesort
    // Although 64-way mergesort will take longer, that doesn't mean that the complexity is any different
    // than standard mergesort
    // Save these timings and plot in whatever tool you like to show the x-axis containing number of elements to sort
    // and the y-axis containing the time it took to sort
    // make sure you are using the same random array for both (make a copy) that way one sort doesn't sort the array
    // and the next sort is looking at presorted data
    // Reminder: T(N) = 2*T(N/2)+N is our recurrence relation for mergesort
    // for k-way: T(N) = K*T(N/K)+N which if you apply case 2 of the master theorem you again have nlogn behavior

}
```

### **Bonus Challenge**
For extra credit, implement:
- A function to **return the number of comparisons** made during sorting.
- A function to **return the total number of merge operations performed**.


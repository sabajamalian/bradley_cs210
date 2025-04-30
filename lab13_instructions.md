
# **Lab 13: BST vs. Red-Black Tree Performance Comparison**

In this lab, you'll investigate the performance differences between a **Binary Search Tree (BST)** and a **Red-Black Tree (RBT)** by inserting and searching a large dataset of contact names. You'll use a provided dataset of 100,000 randomly generated fake contact names and phone numbers, and implement insertions and lookups in both trees. The goal is to observe the performance gap between a simple BST and a self-balancing Red-Black Tree.

---

## **Problem Statement**

You're given a CSV file containing 100,000 fake contact names. Your task is to:

1. Insert all contacts one row at a time into a **standard Binary Search Tree**, using a string key (`last_name,first_name`).
2. Insert the same contacts into a **Red-Black Tree**, using a string key (`last_name,first_name`). 
3. Measure and compare the performance of **lookup operations** on both trees using a set of randomly selected contact names.

---

## **Dataset Format**

You will be provided with a file named `contacts.csv`, formatted as follows:

```
first_name,last_name,phone_number
Michael,Smith,555-0192
Ashley,Jones,555-1444
...
```

Each row represents one contact. You will use `last_name + "," + first_name` as the **lookup key** for your trees.

---

## **Objectives**

By the end of this lab, you should be able to:

1. Implement efficient BST and RBT insertion and lookup.
2. Use templates or class-based structures for general-purpose trees.
3. Benchmark and analyze time complexity with real-world data.
4. Understand why Red-Black Trees outperform simple BSTs on skewed input.

---

## **Approach**

### **1. BST Implementation**

- Use or extend your previous BST code.
- Insert contact names using a string key (`last_name,first_name`).
- Do not self-balance the tree — this is a standard unbalanced BST.

### **2. Red-Black Tree Implementation**

- Use the version from lecture or implement your own Templated version.
- Ensure that your RBT handles balancing via rotations and color flips.
- It is strongly recommended that you **templatize** the tree class for reuse.

### **3. Performance Comparison**

- After inserting all contacts:
  - Randomly select 1,000 contact names from the dataset.
  - Measure the **average time to search** for a contact in the BST vs. the RBT.
  - Report the **total lookup time** and optionally, average depth if implemented.

---

## **Function Signatures**

You should implement the following in `lab13.cpp`:

```cpp
// Insert contact into a BST
void bst_insert(TreeNode*& root, const string& key);

// Insert contact into a Red-Black Tree
void rbt_insert(RBTree& tree, const string& key);

// Search for a contact in BST
bool bst_search(TreeNode* root, const string& key);

// Search for a contact in RBT
bool rbt_search(const RBTree& tree, const string& key);
```

---

## **Main Function Usage**

Your `main()` should:

1. Load the file `contacts.csv`.
2. Construct both:
   - A simple BST
   - A Red-Black Tree
3. Insert **all 100,000 contacts** into each tree.
4. Randomly select **1,000 keys** from the dataset.
5. Time and compare the lookup performance of both trees.

```cpp
int main() {
    vector<string> keys = load_contact_keys("contacts.csv"); // builds "last,first" keys

    TreeNode* bst_root = nullptr;
    RBTree rbt;

    // Insert into BST and RBT
    for (const auto& key : keys) {
        bst_insert(bst_root, key);
        rbt_insert(rbt, key);
    }

    // Shuffle and select random sample
    vector<string> lookup_keys = select_random_keys(keys, 1000);

    // Time lookups
    auto bst_time = time_lookup(bst_root, lookup_keys, bst_search);
    auto rbt_time = time_lookup(rbt, lookup_keys, rbt_search);

    cout << "BST Lookup Time: " << bst_time << " ms\n";
    cout << "RBT Lookup Time: " << rbt_time << " ms\n";

    return 0;
}
```

---


## **Extra Credit (Optional +10%)**

- Measure and report:
  - Average search depth in each tree.
  - Worst-case depth.
  - Insert time per tree.

---

## **Tips and Hints**

- Use `<chrono>` or the previously provided `timer.h` for measuring performance accurately.
- Consider using a templated tree interface to easily switch between BST and RBT.
- Make sure your tree structures handle string keys efficiently.

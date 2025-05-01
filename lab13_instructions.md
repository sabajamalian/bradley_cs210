
# **Lab 13: BST vs. Red-Black Tree Performance Comparison**

In this lab, you'll investigate the performance differences between a **Binary Search Tree (BST)** and a **Red-Black Tree (RBT)** by inserting and searching a large dataset of contact names. You'll use a provided dataset of 100,000 contacts and implement insertions and lookups in both trees. The goal is to observe the performance gap between a simple BST and a self-balancing Red-Black Tree.

---

## **Problem Statement**

You're given a CSV file containing 100,000 fake contact names. Your task is to:

1. Insert all contacts one row at a time into a **standard Binary Search Tree**.
2. Insert the same contacts into a **Red-Black Tree**, using the provided class template or your own implementation.
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

- Use and extend the version discussed during the class.
- Ensure that your RBT handles balancing via rotations and color flips.
- It is strongly recommended that you **templatize** the tree class for reuse.

### **3. Performance Comparison**

- After inserting all contacts:
  - Randomly select 1,000 contact names from the dataset.
  - Measure the **average time to search** for a contact in the BST vs. the RBT.
  - Report the **total lookup time**, **average time**, and display the top 10 slowest lookups for each.

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
5. Measure and compare the lookup performance using per-lookup timing:

```cpp
int main() {
    vector<string> keys = load_contact_keys("contacts.csv"); // builds "last,first" keys

    TreeNode* bst_root = nullptr;
    RBTree rbt;

    for (const auto& key : keys) {
        bst_insert(bst_root, key);
        rbt_insert(rbt, key);
    }

    vector<string> lookup_keys = select_random_keys(keys, 1000);

    vector<double> bst_times, rbt_times;

    for (const auto& key : lookup_keys) {
        auto start = chrono::high_resolution_clock::now();
        bst_search(bst_root, key);
        auto end = chrono::high_resolution_clock::now();
        bst_times.push_back(chrono::duration<double, milli>(end - start).count());

        start = chrono::high_resolution_clock::now();
        rbt_search(rbt, key);
        end = chrono::high_resolution_clock::now();
        rbt_times.push_back(chrono::duration<double, milli>(end - start).count());
    }

    double bst_total = accumulate(bst_times.begin(), bst_times.end(), 0.0);
    double rbt_total = accumulate(rbt_times.begin(), rbt_times.end(), 0.0);

    cout << "BST Total Lookup Time: " << bst_total << " ms\n";
    cout << "RBT Total Lookup Time: " << rbt_total << " ms\n";
    cout << "BST Avg Time: " << bst_total / bst_times.size() << " ms\n";
    cout << "RBT Avg Time: " << rbt_total / rbt_times.size() << " ms\n";

    vector<pair<double, string>> bst_detailed, rbt_detailed;
    for (int i = 0; i < lookup_keys.size(); ++i) {
        bst_detailed.emplace_back(bst_times[i], lookup_keys[i]);
        rbt_detailed.emplace_back(rbt_times[i], lookup_keys[i]);
    }

    sort(bst_detailed.rbegin(), bst_detailed.rend());
    sort(rbt_detailed.rbegin(), rbt_detailed.rend());

    cout << "Top 10 slowest BST lookups:\n";
    for (int i = 0; i < 10; ++i)
        cout << bst_detailed[i].second << " - " << bst_detailed[i].first << " ms\n";

    cout << "Top 10 slowest RBT lookups:\n";
    for (int i = 0; i < 10; ++i)
        cout << rbt_detailed[i].second << " - " << rbt_detailed[i].first << " ms\n";

    return 0;
}
```

---

## **Helper Functions (Suggested)**

```cpp
vector<string> load_contact_keys(const string& filename);
vector<string> select_random_keys(const vector<string>& keys, int count);
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

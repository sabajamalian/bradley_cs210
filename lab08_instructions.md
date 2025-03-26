# **Lab 08: Construct Binary Search Tree from Preorder and Inorder Traversal**

In this lab, you will reconstruct a **Binary Search Tree (BST)** using its **preorder** and **inorder** traversals. This classic problem highlights the power of **divide and conquer**, which is a fundamental technique (better to say "strategy") that recursively breaks a problem into subproblems and solves each part effectively.

---

## **Problem Statement**

You are given two integer arrays: `preorder` and `inorder`. These arrays represent the preorder and inorder traversals of a **Binary Search Tree (BST)**. Your task is to **reconstruct** the original BST and return its root. Feel free to re-use the BST structs from the previous labs. 

### **Definitions:**

- **Preorder Traversal (Root → Left → Right):** First visit the root, then left subtree, then right.
- **Inorder Traversal (Left → Root → Right):** First visit the left subtree, then the root, then right.
- For a **BST**, the inorder traversal always produces a **sorted array**.

---

### **Example**

#### **Input:**
```
preorder = [8, 5, 1, 7, 10, 12]
inorder  = [1, 5, 7, 8, 10, 12]
```

#### **Output (Binary Search Tree Structure):**
```
        8
       / \
      5   10
     / \    \
    1   7    12
```

---

## **Objectives**

By the end of this lab, you should be able to:

1. Understand the relationship between preorder and inorder traversals in a BST.
2. Apply divide and conquer techniques to tree construction.
3. Develop a recursive solution to efficiently build the BST.

---

## **Why Divide and Conquer?**

This problem is ideal for divide and conquer because:

- The **first value in preorder** is always the **root**.
- In the **inorder traversal**, everything **to the left of the root** is in the left subtree, and everything **to the right** is in the right subtree.
- We can **recursively** build each subtree using this information.

Each recursive step handles a smaller subproblem of the tree.

---

## **Approach**

### **Thought Process:**

1. Identify the root from the start of the preorder array.
2. Find the root's position in the inorder array.
3. Split the inorder array into left and right subtrees.
4. Use the size of the left subtree to split the preorder array.
5. Recursively build left and right subtrees.

---

## **Pseudocode**

```
Function buildTree(preorder, inorder):
    if preorder is empty or inorder is empty:
        return null

    root_val = preorder[0]
    root = new TreeNode(root_val)

    root_index = index of root_val in inorder

    left_inorder = inorder[0 : root_index]
    right_inorder = inorder[root_index + 1 :]

    left_preorder = preorder[1 : 1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder) :]

    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)

    return root
```

---

## **Function Signature**

You will implement the following function in C++:

```cpp
TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder);
```

---

## **Main Function**

Use this to test your implementation:

```cpp
int main() {
    vector<int> preorder = {8, 5, 1, 7, 10, 12};
    vector<int> inorder = {1, 5, 7, 8, 10, 12};

    TreeNode* root = buildTree(preorder, inorder);

    // Optional: Write a traversal to print the tree and verify structure
    return 0;
}
```

---

## **Challenge (10% extra credit)**

- What is the time complexity of this solution?
- How could you optimize it using a **hash map** for fast lookups of root indices in inorder?



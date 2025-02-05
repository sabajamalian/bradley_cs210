# **Lab 02: Implementing Binary Search Tree (BST) Traversals**

In this lab, you will build on your understanding of **Binary Search Trees (BSTs)** by implementing the three main traversal methods:
- **Preorder Traversal** (Root → Left → Right)
- **Postorder Traversal** (Left → Right → Root)
- **Level Order Traversal** (Breadth-First, using a Queue)

These traversal methods are essential for understanding how to navigate and manipulate BSTs efficiently.

---

## **Objectives**
By the end of this lab, you should:
1. Understand the structure of a **Binary Search Tree**.
2. Learn how **Preorder, Postorder, and Level Order Traversals** work.
3. Implement each of these traversal methods step by step.
4. Use a **Queue** for Level Order Traversal.

---

## **Part 1: Understanding BST Traversals**

A **Binary Search Tree (BST)** is a hierarchical data structure in which:
- The **left child** of a node contains values **less than** the node's value.
- The **right child** of a node contains values **greater than** the node's value.

### **Preorder, Postorder, and Level Order Traversals**

| Traversal Type  | Order |
|-----------------|-------------------------|
| **Preorder**    | Root → Left → Right |
| **Postorder**   | Left → Right → Root |
| **Level Order** | Level by Level (Breadth-First, using a Queue) |

For example, given the BST:

```
        10
       /  \
      5    15
     / \   / \
    3   7 12  18
```

- **Preorder Traversal Output**: `10 5 3 7 15 12 18`
- **Postorder Traversal Output**: `3 7 5 12 18 15 10`
- **Level Order Traversal Output**: `10 5 15 3 7 12 18`

---

## **Part 2: Implementing Preorder Traversal**

### **Understanding Preorder Traversal**
Preorder traversal follows the order:  
**Root → Left Subtree → Right Subtree**

Steps to implement:
1. Start at the **root** node.
2. **Print** the current node's value.
3. Recursively **traverse the left subtree**.
4. Recursively **traverse the right subtree**.

### **Implement the `preorderTraversal` Function**
- Define a **recursive function** to perform preorder traversal.
- Call the function from the **BST class**. Use the code snippet reviewed in the class.

---

## **Part 3: Implementing Postorder Traversal**

### **Understanding Postorder Traversal**
Postorder traversal follows the order:  
**Left Subtree → Right Subtree → Root**

Steps to implement:
1. Start at the **leftmost node** and traverse to the right.
2. **Visit the left subtree recursively**.
3. **Visit the right subtree recursively**.
4. **Print the root node's value**.

### **Implement the `postorderTraversal` Function**
- Define a **recursive function** to perform postorder traversal.
- Call the function from the **BST class**. Use the code snippet reviewed in the class.

---

## **Part 4: Implementing Level Order Traversal**

### **Understanding Level Order Traversal**
Level order traversal (also known as **Breadth-First Traversal**) visits nodes **level by level** from top to bottom.

Steps to implement:
1. Use a **Queue** data structure to store tree nodes.
2. **Enqueue the root node** into the queue.
3. **While the queue is not empty**:
   - **Dequeue** the front node and print its value.
   - **Enqueue** the left child (if it exists).
   - **Enqueue** the right child (if it exists).

### **Implement the `levelOrderTraversal` Function**
- Use a **Queue** to handle traversal. 
- Print nodes as they are dequeued. Use the code snippet reviewed in the class.

---

## **Expected Output**
When you run the program, it should display:

```
Preorder Traversal: 10 5 3 7 15 12 18
Postorder Traversal: 3 7 5 12 18 15 10
Level Order Traversal: 10 5 15 3 7 12 18
```

---

## **Bonus Challenge**
For 10% bonus points, try adding:
- A function to **find the height of the BST**.
- A function to **count the total number of nodes**.


# CS210: Project Milestone 3 Requirements

In this milestone, you will extend your previous implementation by replacing the linked list data structure with a **Binary Search Tree (BST)**. You will store school data from a CSV file in a BST and implement functions for inserting, deleting, and searching school records efficiently. 
Create a new directory in your repository for this milestone so you can keep your previous Linked List implementations. However, feel free to 
reuse some of the code you had from the previous milestone, including the CSV reading part and the School struct.

---

## Understanding Binary Search Trees
A **Binary Search Tree (BST)** is a hierarchical data structure in which each node has at most two children:
- The **left child** contains nodes with values less than the parent node.
- The **right child** contains nodes with values greater than the parent node.

BSTs provide efficient operations for searching, insertion, and deletion in O(log n) time on average.

---

## Your Task

### 1. Implement a Binary Search Tree (BST)
Create a BST class named `SchoolBST` with the following functions:

#### **Insertion**
- **`insert(School school)`**: Insert a new school into the BST. Use the school name as the key for ordering nodes.

#### **Deletion**
- **`deleteByName(string name)`**: Delete a school node by its name. Handle all three deletion cases:
  1. Node with no children (leaf node).
  2. Node with one child.
  3. Node with two children (find the in-order successor or predecessor to replace the node).

#### **Search**
- **`findByName(string name)`**: Search for a school by its name and return the school information.

#### **Display**
- **`displayInOrder()`**: Print the schools in alphabetical order by name (in-order traversal).
- **`displayPreOrder()`**: Print the schools in pre-order traversal.
- **`displayPostOrder()`**: Print the schools in post-order traversal.

### 2. Load Data into the BST
Read the school records from a CSV file and insert each school into the BST.

### 3. Test Your Implementation
Write a `main()` function that:
- Loads the CSV file.
- Inserts all school records into the BST.
- Allows the user to search for a school by name.
- Allows the user to delete a school by name.
- Displays the schools using different traversal methods.

### 4. Commit Incrementally and Often
Your code should be inside the repository you created in milestone 1. As you write code, make periodic commits to track your progress and maintain version control. Regular commits will document your development process and help in debugging.

---

## Future Milestones
In upcoming milestones, you will:
- Implement a **Hash Table** for school data storage.
- Compare the performance of BST, Linked List, and Hash Table.
- Work with larger datasets covering Illinois and USA schools.

---

## Rubric and Scoring
Your project will be graded based on the following criteria:
- **Correct implementation of insert function (`insert`) (20 points)**
- **Correct implementation of delete function (`deleteByName`) (20 points)**
- **Correct implementation of search function (`findByName`) (20 points)**
- **Properly loading data from CSV and displaying results using BST traversal (20 points)**
- **Version control and commit history (20 points)**: Ensure structured and periodic commits demonstrating development steps.

---

## Submission Guidelines
- Provide a link to your repository.

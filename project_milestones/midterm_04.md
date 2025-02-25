# CS210: Project Milestone 4 Requirements

In this milestone, you will implement a **Hash Table** data structure. You will store school data from a CSV file in a hash table and implement functions for inserting, deleting, and searching school records efficiently. Create a new directory for this milestone in your repository and 
feel free to re-use code from the previous milestones.

---

## Understanding Hash Tables
A **Hash Table** is a data structure that maps keys to values using a hash function. It provides efficient O(1) average-time complexity for search, insertion, and deletion operations.

- A **hash function** computes an index from the key (school name) to store data in an array.
- **Collision handling** methods such as **separate chaining (linked lists)** or **open addressing** (e.g., linear probing) manage cases where multiple keys map to the same index.

### Choosing a Hash Function
A good hash function should distribute keys uniformly to avoid collisions. Here are some commonly used hash functions:

1. **Modulo Hashing:** Convert characters of the string into ASCII values, sum them, and take modulo of the table size:
   ```cpp
   int hashFunction(string key, int tableSize) {
       int hash = 0;
       for (char ch : key) {
           hash += ch;
       }
       return hash % tableSize;
   }
   ```

2. **Polynomial Rolling Hash:** Uses a prime number as a base to minimize collisions:
   ```cpp
   int polynomialHash(string key, int tableSize, int prime = 31) {
       long hash = 0;
       long power = 1;
       for (char ch : key) {
           hash = (hash + (ch - 'a' + 1) * power) % tableSize;
           power = (power * prime) % tableSize;
       }
       return hash;
   }
   ```

You are encouraged to design your own hash function and experiment with different approaches!

---

## Your Task

### 1. Implement a Hash Table
Create a class named `SchoolHashTable` with the following functions:

#### **Insertion**
- **`insert(School school)`**: Insert a new school into the hash table using the school name as the input to your hash function and calculate the key.

#### **Deletion**
- **`deleteByName(string name)`**: Delete a school node by its name from the hash table.

#### **Search**
- **`findByName(string name)`**: Search for a school by its name and return the school information.

#### **Display**
- **`display()`**: Print all stored schools, showing how data is distributed across the hash table.

### 2. Load Data into the Hash Table
Read the school records from a CSV file and insert each school into the hash table.

### 3. Test Your Implementation
Write a `main()` function that:
- Loads the CSV file.
- Inserts all school records into the hash table.
- Allows the user to search for a school by name.
- Allows the user to delete a school by name.
- Displays the stored schools and their positions in the hash table.

### 4. Commit Incrementally and Often
Your code should be inside the repository you created in milestone 1. As you write code, make periodic commits to track your progress and maintain version control. Regular commits will document your development process and help in debugging.

---

## Future Milestones
In the upcoming and milestone, you will:
- Compare the performance of Hash Table, Binary Search Tree, and Linked List.
- Work with larger datasets covering Illinois and USA schools.

---

## Rubric and Scoring
Your project will be graded based on the following criteria:
- **Correct implementation of insert function (`insert`) (20 points)**
- **Correct implementation of delete function (`deleteByName`) (20 points)**
- **Correct implementation of search function (`findByName`) (20 points)**
- **Properly loading data from CSV and displaying results (20 points)**
- **Version control and commit history (20 points)**: Ensure structured and periodic commits demonstrating development steps.

---

## Submission Guidelines
- Provide a link to your repository.

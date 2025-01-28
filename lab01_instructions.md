
# **Lab 01: Implementing a Doubly Linked List**

In this lab, you will build a **Doubly Linked List (DLL)** by extending the ideas from the **Singly Linked List (SLL)** implementation. Follow the instructions carefully, and don’t hesitate to ask for help if you get stuck.

---

## **Objectives**
By the end of this lab, you should:
1. Understand the structure of a **Doubly Linked List**.
2. Learn how to add forward and backward links between nodes.
3. Implement key operations such as appending, printing the list in both directions, and deleting nodes.

---

## **Part 1: Review of the Singly Linked List Code**

Examine the provided Singly Linked List code below. Understand:
- How the `Node` structure works.
- How the `append` function adds new elements to the list.
- How the `printList` function iterates through the list to display its elements.

### **Singly Linked List Code**
```cpp
#include <iostream>
using namespace std;

template<typename T>
struct Node
{
    T data;
    Node* next;
    Node(T val) : data(val), next(nullptr) {}
};

template<typename T>
class SinglyLinkedList
{
    Node<T>* head;

public:
    SinglyLinkedList() : head(nullptr) {}

    void append(T data)
    {
        Node<T>* newNode = new Node<T>(data);
        if(head==nullptr)
        {
            head = newNode;
        }else
        {
            Node<T>* temp = head;
            while(temp->next != nullptr)
            {
                temp = temp->next;
            }
            temp->next = newNode;
        }
    }
    void printList()
    {
        Node<T>* temp = head;
        while(temp!=nullptr)
        {
            cout << temp->data << " -> ";
            temp = temp->next;
        }
        cout << "nullptr" << endl;
    }
};

int main()
{
    SinglyLinkedList<int> list;
    list.append(12);
    list.append(14);
    list.append(23);
    list.append(-7);
    list.append(31);
    list.printList();
}
```

---

## **Part 2: Transition to a Doubly Linked List**

In a Doubly Linked List, each node contains:
1. A **data field** to store the value.
2. A **`next` pointer** to the next node in the list.
3. A **`prev` pointer** to the previous node in the list.

---

## **Steps to Implement the Doubly Linked List**

### **Step 1: Append and Print Operations**
1. **Define a Doubly Linked Node (`DNode`)**:
   - Create a struct similar to `Node`, but with an additional `prev` pointer.
   - Initialize both `next` and `prev` pointers in the constructor.

2. **Update the Linked List Class**:
   - Modify the class to use the new `DNode`.
   - Add functionality for both forward and backward traversal of the list.

3. **Write the `append` Function**:
   - Adjust the logic to set both `next` and `prev` pointers when appending a new node.

4. **Add a `printListReverse` Function**:
   - Implement a function that starts from the last node and prints the list in reverse order using the `prev` pointers.

### **Step 2: Implement a Delete Operation**
1. Add a `delete` function to the `DoublyLinkedList` class.
   - It should take a value `data` as input and delete the first node containing that value.
   - Update the `prev` and `next` pointers of adjacent nodes to maintain the structure of the doubly linked list.
   - Consider edge cases:
     - Deleting the head node.
     - Deleting the tail node.
     - Deleting the only node in the list.
     - Deleting a value that doesn’t exist in the list.

---

## **Expected Output**
When you run the program, it should display:

```
List (forward): 12 -> 14 -> 23 -> -7 -> 31 -> nullptr
List (reverse): 31 -> -7 -> 23 -> 14 -> 12 -> nullptr
Deleting 23...
List after deletion (forward): 12 -> 14 -> -7 -> 31 -> nullptr
List after deletion (reverse): 31 -> -7 -> 14 -> 12 -> nullptr
```

---

Feel free to extend the implementation with additional operations (e.g., inserting at a specific position) for extra practice!

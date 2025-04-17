# **Lab 11: Huffman Coding – Greedy Algorithms**

In this lab, you'll explore a classic **greedy algorithm** that compresses data efficiently using **Huffman Coding**. You’ll implement the core logic of Huffman coding using **priority queues (min-heaps)** and **binary trees**.

---

## **Problem Statement**

You're given a mapping of characters and their frequencies. Your task is to:

1. **Build a Huffman Tree** from the frequency table.
2. **Generate Huffman codes** for each character by traversing the tree.
3. (Optional for extra credit) **Decompress a Huffman-encoded string** back to its original form.

---

## **Example**

### **Input Frequencies:**
```
a: 5, b: 9, c: 12, d: 13, e: 16, f: 45
```

### **Expected Huffman Codes (example, may vary):**
```
f: 0
c: 100
d: 101
a: 1100
b: 1101
e: 111
```

---

## **Objectives**

By the end of this lab, you should be able to:

1. Understand the greedy approach behind Huffman coding.
2. Use a **min-heap** to build trees efficiently.
3. Apply **tree traversal** to generate binary codes for characters.

---

## **Approach**

1. **Build the Huffman Tree** using a min-heap (priority queue):
   - Create a leaf node for each character and push it into the heap.
   - While there is more than one node in the heap:
     - Remove the two nodes with the lowest frequency.
     - Create a new node with these two as children and insert it back.
   - The last remaining node is the **root** of the Huffman Tree.

2. **Generate Codes** by traversing the tree:
   - Use DFS to assign `'0'` for left edges and `'1'` for right edges.
   - Concatenate the bits as you traverse to build the full code for each character.

3. **(Extra Credit)** Decompress a binary string using the Huffman Tree.

---

## **Function Signatures**

Implement the following functions in `huffman.cpp`:

```cpp
// REQUIRED: Generate the Huffman codes for each character
void generateCodes(Node* root, string code, unordered_map<char, string>& huffmanCode);

// REQUIRED: Build the Huffman Tree from character frequencies
Node* buildHuffmanTree(unordered_map<char, int>& freq);

// OPTIONAL (Extra Credit +35): Decode the Huffman-encoded string
string decompress(Node* root, const string& encoded);
```

---

## **Provided Structures & Boilerplate**

Here’s a sample structure and setup to help you get started. 

```cpp
struct Node {
    char ch;
    int freq;
    Node *left, *right;

    Node(char c, int f) : ch(c), freq(f), left(nullptr), right(nullptr) {}
};

// Custom comparator for priority queue (min-heap)
struct compare {
    bool operator()(Node* l, Node* r) {
        return l->freq > r->freq;
    }
};
```

You can use the STL min-heap like this:
```cpp
priority_queue<Node*, vector<Node*>, compare> minHeap;
```

---

## **Main Function (Sample Usage)**

Use this code to test your implementation:

```cpp
int main() {
    unordered_map<char, int> freq = {
        {'a', 5}, {'b', 9}, {'c', 12},
        {'d', 13}, {'e', 16}, {'f', 45}
    };

    Node* root = buildHuffmanTree(freq);

    unordered_map<char, string> huffmanCode;
    generateCodes(root, "", huffmanCode);

    cout << "Huffman Codes:\n";
    for (auto pair : huffmanCode) {
        cout << pair.first << ": " << pair.second << "\n";
    }

    // Example string encoding
    string text = "abcdef";
    string encoded = "";
    for (char ch : text) {
        encoded += huffmanCode[ch];
    }

    cout << "\nEncoded string:\n" << encoded << "\n";

    // EXTRA CREDIT: Decompressing
    cout << "\nDecoded string:\n" << decompress(root, encoded) << "\n";

    return 0;
}
```

---

## **Challenge (35% Extra Credit)**

- Implement the **decompress** function to decode a Huffman-encoded binary string.
- Think about performance: can you decode in a single pass through the string?
- How could you extend this to handle files, or a binary format?

---

## **Appendix: HeapSort Example (Just for Familiarity)**

Here's an example of using `priority_queue` as a min-heap. This isn't part of the lab, but it can help if you're unfamiliar with STL heaps.

```cpp
priority_queue<int, vector<int>, greater<int>> minHeap;
vector<int> data = {5, 1, 9, 3, 7};

for (int n : data) minHeap.push(n);
while (!minHeap.empty()) {
    cout << minHeap.top() << " ";
    minHeap.pop();
}
```

# **Lab 12: Traveling Salesman Problem**

In this lab, you'll implement and compare two solutions to the **Traveling Salesman Problem (TSP)**, a classic graph optimization challenge. One will be a brute-force exact method, and the other a fast **greedy approximation** using **Minimum Spanning Trees (MSTs)**.

---

## **Problem Statement**

Bradley's campus Wi-Fi is down (fictional setting). You must plan a round-trip tour starting from a selected building, visiting several others, and returning to the start. Your goal is to:

1. **Compute the exact shortest tour** using a brute-force approach.
2. **Approximate the shortest tour** using a MST-based greedy algorithm (Prim’s + DFS).
3. (Optional for extra credit) **Generate a KML file** to visualize both tours in Google Earth.

---

## **Example**

### **Input Buildings (Subset):**
```
1: One World
2: Hartmann Center
3: Markin Family Student Recreation Center
4: Morgan Hall
```

### **Sample Output:**
```
Brute-force TSP Path: 1 -> 2 -> 4 -> 3 -> 1
Distance: 10.93 meters

Approximate TSP Path (via MST + DFS): 1 -> 2 -> 3 -> 4 -> 1
Distance: ~11.04 meters
```

---

## **Objectives**

By the end of this lab, you should be able to:

1. Use Euclidean distance to compute graph weights.
2. Generate all permutations for brute-force TSP.
3. Apply Prim’s algorithm using a **min-heap** to build MSTs.
4. Traverse MST with DFS to approximate a Hamiltonian cycle.

---

## **Approach**

### **1. Brute Force TSP**

- Generate all permutations of the buildings to visit (starting and ending at the first location).
- Calculate the total tour distance for each permutation.
- Track the minimum distance and path.

### **2. TSP Approximation via MST**

- Use Prim’s algorithm to build a MST.
- Traverse the MST using DFS.
- Form a cycle by returning to the start.
- This approximates the shortest Hamiltonian cycle.

### **3. Extra Credit: KML Output**

- Generate a `.kml` file showing both TSP paths using Google Earth compatible format.
- Use latitude/longitude from the input file.
- Use distinct colors and optionally offset paths vertically to differentiate.

---

## **Function Signatures**

Implement the following functions in `hw4.cpp`:

```cpp
// REQUIRED: Brute force TSP solver
double tsp_bruteforce(const vector<Place>& places, vector<int>& path);

// REQUIRED: Approximation TSP using MST and DFS
double tsp_approx(const vector<Place>& places, vector<int>& path);

// OPTIONAL: Generate KML file to visualize tours
void make_kml(const string& filename, const vector<Place>& places, const vector<int>& brute_path, const vector<int>& approx_path);
```

---

## **Main Function Usage**

Your program should:
1. Load data from `bradley.txt`.
2. Prompt the user for locations to visit.
3. Run both TSP algorithms and display:
   - The path and distance for brute-force.
   - The path and distance for the MST approximation.
4. (Extra Credit) Write the paths to `hw4.kml`.

---

## **Challenge (20% Extra Credit)**

- Write the TSP paths to a **KML file**.
- Customize with colors, height offsets, and labels.
- Test in Google Earth for visualization.

---

## **Appendix: Heap Usage**

Prim’s algorithm should use a **priority_queue** for edge selection.

```cpp
priority_queue<pair<double, int>, vector<pair<double, int>>, greater<>> minHeap;
```

Use this queue to efficiently grow your MST.
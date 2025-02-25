# CS210: Project Milestone 2 Requirements

In this milestone, you will load school data from a CSV file into a linked list using C++. You will implement a linked list data structure for storing and managing school information. As part of this data structure, you will implement functions for inserting new schools, deleting a school by name, and finding a school by name.

## A CSV File
A **Comma-Separated Values (CSV) file** is a plain text file that stores tabular data. Each line represents a row, and values are separated by commas. The first row usually contains headers describing the data.

Example CSV format:
```
NAME,ADDRESS,CITY,STATE,COUNTY
KELLAR PRIMARY SCHOOL,6413 MT HAWLEY RD,PEORIA,IL,PEORIA
FRANKLIN PRIMARY SCHOOL,807 W COLUMBIA TER,PEORIA,IL,PEORIA
PLEASANT VALLEY MIDDLE SCHOOL,3314 W RICHWOODS BVD,PEORIA,IL,PEORIA
...
```

Here is a code snippet that reads the CSV file line by line, splits each line by commas, and prints the parsed data. You can integrate this with your own linked list structure or choose to implement your own C++ code to read data from a CSV. 

```cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

class CSVReader {
public:
    static vector<vector<string>> readCSV(const string& filename) {
        ifstream file(filename);
        vector<vector<string>> data;
        string line, word;

        if (!file.is_open()) {
            cerr << "Error: Could not open file " << filename << endl;
            return data;
        }

        while (getline(file, line)) {
            stringstream ss(line);
            vector<string> row;
            while (getline(ss, word, ',')) {
                row.push_back(word);
            }
            data.push_back(row);
        }
        file.close();
        return data;
    }
};

```

## Your Task
### 1. Define the `School` Struct
Define a struct named `School` that includes the following attributes:
- `name` (string)
- `address` (string)
- `city` (string)
- `state` (string)
- `county` (string)
- Pointer to the next node in the linked list

### 2. Implement a Singly Linked List
Create a linked list class named `SchoolList` with the following functions:
- **`insertFirst(School school)`**: Insert a new school at the beginning of the list.
- **`insertLast(School school)`**: Insert a new school at the end of the list.
- **`deleteByName(string name)`**: Delete a school node by its name.
- **`findByName(string name)`**: Search for a school by its name and return the school information.
- **`display()`**: Print the list of schools.

### 3. Load Data into the Linked List
Load data and insert each school into the linked list.

### 4. Test Your Implementation
Write a `main()` function that:
- Loads the CSV file.
- Inserts all school records into the linked list.
- Allows the user to search for a school by name.
- Allows the user to delete a school by name.
- Displays the list of remaining schools.

### 5. Commit incrementally and often
Your code should be inside the repository you created in milestone 1. As you write code, make periodic commits to track your progress and maintain version control. This practice will help you manage different stages of development, revert changes if needed, and demonstrate your coding development steps effectively. Regular commits also provide a clear history of modifications, which is crucial for debugging and collaboration.

This project is part of a larger series. In upcoming milestones, you will:
- Implement other data structures (Binary Search Trees and Hash Tables).
- Work with larger datasets, including Illinois and USA schools.
- Compare the performance of these data structures on every operation.

## Rubric and Scoring
Your project will be graded based on the following criteria:
- **Correct implementation of insert functions (`insertFirst` and `insertLast`) (20 points)**
- **Correct implementation of delete function (`deleteByName`) (20 points)**
- **Correct implementation of search function (`findByName`) (20 points)**
- **Properly loading data from CSV and displaying the list (20 points)**
- **Version control and commit history (20 points)**: Your repository should show periodic commits tracking your development progress. Ensure that each major step is committed separately, demonstrating structured coding and debugging steps.

## Submission Guidelines
- Provide a link to your repository. 

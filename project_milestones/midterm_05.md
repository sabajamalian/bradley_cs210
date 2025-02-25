# CS210: Project Milestone 5 Requirements

In this final milestone, you will evaluate the efficiency of the three data structures implemented in previous milestones (**Linked List, Binary Search Tree, and Hash Table**) by running your code on larger datasets and analyzing runtime performance. You will generate runtime comparisons, visualize your findings in charts, and write a structured report.

---

## Larger Datasets
Previously, you worked with `Illinois_Peoria_Schools.csv`. In this milestone, you will be provided with two larger datasets:
- **`Illinois_Schools.csv`** (Contains all schools in Illinois)
- **`USA_Schools.csv`** (Contains schools from across the United States)

Your goal is to run all implemented operations on these datasets and compare their performance across different data structures.

---

## Your Task

### 1. Implement Runtime Analysis
You will measure the time taken for each of the following operations in **Linked List, Binary Search Tree, and Hash Table**:
- **Insertion**
- **Deletion by Name**
- **Search by Name**

Use the provided `Timer.h` file to measure execution time, or implement your own timing mechanism in C++.

### 2. Generate Charts for Comparison
Use a tool like **Excel or Google Sheets** to visualize runtime performance for each operation across different data structures. Your charts should include:
- **Bar charts comparing insertion, deletion, and search times.**
- **Line graphs to analyze performance trends across increasing dataset sizes.**

### 3. Write a Performance Analysis Report
Prepare a **minimum 2-page report** detailing:
- Your methodology for testing and timing functions.
- Observations on which data structure performed best and why.
- Challenges encountered and improvements that could be made.
- Interpretation of charts and comparison of runtimes.

Your report should be well-structured, including:
- **Introduction**
- **Experiment Setup** (Datasets, Tools, and Methodology)
- **Results and Analysis** (Charts & Discussion)
- **Conclusion** (Best Data Structure for the Problem)

---

## Commit Incrementally and Often
Your code should be inside the repository you created in milestone 1. As you write code, make periodic commits to track your progress and maintain version control. Regular commits will document your development process and help in debugging.

---

## Rubric and Scoring
Your project will be graded based on the following criteria:
- **Correct implementation of timing analysis (20 points)**
- **Proper generation and visualization of runtime comparison charts (20 points)**
- **Detailed report analyzing runtime results (30 points)**
- **Proper execution of dataset processing (20 points)**
- **Version control and commit history (10 points)**

---

## Submission Guidelines
- Provide a link to your repository.
- Submit your runtime charts and analysis report as a PDF file.

# CS210: Final Project Milestone 4 Requirements

In this final milestone, you will conduct a **performance analysis** of your city population lookup program using various caching strategies. You will write a **separate load testing script** that simulates user queries, measure the program’s performance under different conditions, and write a **report** analyzing the results.

## Objective

Your goals for Milestone 4 are to:
- Build an automated testing script that simulates a high volume of lookups.
- Run performance tests using each of the three caching algorithms (LFU, FIFO, Random Replacement).
- Measure and record performance metrics such as average lookup time and cache hit ratio.
- Write a short report analyzing and comparing the results.

## Your Task

### 1. Write a Load Testing Script

Create a **separate C++ script** that:
- Generates or reads a sequence of city name and country code queries (at least 500–1000 lookups).
- Feeds these queries to your main program (Milestone 3) or simulates the same logic internally.
- Records the time taken for each lookup and whether it was a cache hit or miss.

You may:
- Use randomized selections of city queries (with some repeated queries to test cache behavior).
- Log performance data such as total time, average time per lookup, and cache statistics.

### 2. Test Each Caching Strategy

Run your script **separately** for each caching strategy:
- LFU (Least Frequently Used)
- FIFO (First-In, First-Out)
- Random Replacement

Make sure to:
- Use the same query dataset for each run.
- Reset the cache between each run.

### 3. Analyze the Results

Compare the performance of the three strategies based on:
- **Average lookup time**
- **Cache hit rate**
- **Consistency across repeated runs**

You may present results using tables or charts for clarity.

### 4. Write a Report

Create a report document (`analysis_report.md` or `analysis_report.pdf`) that includes:
- A brief explanation of your testing methodology.
- Tables or graphs summarizing the performance metrics.
- Your observations about the strengths and weaknesses of each caching strategy.
- A conclusion discussing which strategy you would recommend and why.

Keep the report professional, clear, and concise (2–3 pages or equivalent in Markdown).

### 5. Version Control

- Include the load testing script and report in your existing GitHub repository.
- Commit all new files with appropriate messages.
- Optionally, tag the final submission as `milestone-4`.

## Rubric and Scoring

Your project will be graded based on the following criteria:

- **Correct and complete load testing script (25 points)**
- **Testing with all three caching strategies (20 points)**
- **Accurate and insightful performance analysis (20 points)**
- **Well-structured and clearly written report (20 points)**
- **Clean code, proper logging, and metrics collection (10 points)**
- **Version control and submission completeness (5 points)**

## Submission Guidelines

- Submit the final GitHub repository link with:
  - Load testing script
  - Performance analysis report
  - All code and documentation for Milestones 1–4

# CS210: Final Project Milestone 2 Requirements

In this second milestone, you will extend your Milestone 1 project by implementing **multiple cache replacement strategies**. Specifically, your program will support **Least Frequently Used (LFU)**, **First-In, First-Out (FIFO)**, and **Random Replacement** caching algorithms. This milestone will help you understand how different caching strategies affect performance and behavior.

## Objective

Enhance your city population lookup program to support three different cache replacement policies:
- **LFU (Least Frequently Used)**
- **FIFO (First-In, First-Out)**
- **Random Replacement**

The user should be able to select which caching strategy to use at the beginning of the program. Once selected, that strategy will be used for all lookups during that session.

## Your Task

### 1. Refactor Existing Cache Code
Adapt your existing cache implementation to support **multiple caching strategies**. You may use inheritance, templates, or other modular designs to structure your code and avoid duplication.

Each strategy should:
- Store up to **10** city population entries.
- Use a data structure that supports the specific eviction policy efficiently.
- Ensure **O(1)** time for cache hits.

### 2. Implement Caching Strategies

#### A. **LFU (Least Frequently Used)**
- Evict the item with the **lowest access frequency** when the cache is full.
- If multiple items have the same frequency, evict the **oldest** among them.
- Update frequency counters on each access (whether cache hit or cache miss).

#### B. **FIFO (First-In, First-Out)**
- Evict the **oldest inserted** item when the cache reaches size 10.
- Do not consider access frequency, only insertion order matters.

#### C. **Random Replacement**
- When the cache is full, randomly select and evict one entry to make space for a new one.
- Access patterns do not influence replacement decisions.

### 3. User Interaction

Update your program so that:
- When it starts, the user is asked to choose one of the three caching strategies.
- The selected strategy is used for all population lookups in that session.
- The user can continue to search for city populations as before.

### 4. Testing

Thoroughly test each caching strategy:
- Verify correct behavior when the cache fills up and evictions occur.
- Print/log the contents of the cache after each operation to validate eviction patterns.
- Test for both cache hits and misses to ensure counters and orderings are accurate.

### 5. Version Control

Continue using the same GitHub repository from Milestone 1:
- Make **incremental commits** for each new feature (e.g., LFU, FIFO, Random).
- Write **clear and descriptive commit messages** explaining the logic behind your design choices and implementations.

## Rubric and Scoring

Your project will be graded based on the following criteria:

- **Correct implementation of LFU caching (20 points)**
- **Correct implementation of FIFO caching (20 points)**
- **Correct implementation of Random Replacement caching (20 points)**
- **User selection and integration of cache strategies (15 points)**
- **Efficient and modular code design (15 points)**
- **Version control with clear, incremental commits (10 points)**

## Submission Guidelines

- Submit an updated link to your GitHub repository showing Milestone 2 work.
- Be sure your repo includes:
  - Updated and clearly separated code for all caching strategies
  - Commit history demonstrating incremental development

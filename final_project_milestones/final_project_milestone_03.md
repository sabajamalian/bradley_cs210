# CS210: Final Project Milestone 3 Requirements

In this third milestone, you will improve the efficiency of city population lookups by loading the dataset into a **Trie (prefix tree)**. A Trie allows for fast, prefix-based searches and will significantly enhance the performance of your application compared to repeated file reads.

## Objective

Modify your application to:
- Load the contents of the `world_cities.csv` file into a **Trie** data structure at startup.
- Use the Trie to efficiently look up city population data based on the **city name and country code**.
- Continue supporting the caching strategies (LFU, FIFO, Random) implemented in Milestone 2 but read data from Trie instead of file when cache is missed. 

## Your Task

### 1. Implement the Trie

Build a Trie that:
- Stores all city names (as keys) and their associated data (country code and population).
- Supports efficient search by exact city name and country code.
- Handles cities with the same name but different country codes.

You may structure the Trie to store a map at each terminal node mapping country code + city name to population.

### 2. Load Data into the Trie

At program startup:
- Read the entire `world_cities.csv` file once.
- Insert each record into the Trie.
- Do **not** re-read the CSV file for each user query.

### 3. Modify Lookup Logic

Change your lookup process to:
- Accept a city name and country code from the user.
- Check cache for the inquiry. 
- If not in cache, search the Trie for the city name and retrieve the corresponding population based on country code.
- Use the caching strategy selected at startup to store and retrieve recent lookups.

### 4. Maintain Cache Functionality

All cache-related logic should continue to function exactly as in Milestone 2. This includes:
- User selection of LFU, FIFO, or Random Replacement strategy.
- Caching the most recent 10 lookups.
- Printing/logging cache contents for testing and debugging.

### 5. User Interaction

Ensure your program continues to:
- Prompt the user for city name and country code.
- Return and display the city’s population.
- Use the Trie for data lookup and the selected cache for optimization.
- Allow the user to exit the program at any time.

### 6. Testing

Test your application to ensure:
- The Trie correctly loads and retrieves all city data.
- Lookups return correct results for cities with similar names or multiple entries.
- The cache still functions as expected.

Use print/log statements to show:
- Trie loading progress (optional).
- Cache hits/misses.
- Evictions and insertions.

### 7. Version Control

Continue using the same GitHub repository:
- Commit frequently with meaningful messages.
- Clearly mark milestones with tags or commit descriptions.

## Rubric and Scoring

Your project will be graded based on the following criteria:

- **Correct and complete implementation of the Trie (30 points)**
- **Proper loading of city data into the Trie (15 points)**
- **Accurate and efficient lookup using city and country code (15 points)**
- **Continued correct behavior of caching strategies (20 points)**
- **Clean, maintainable, and modular code design (10 points)**
- **Version control with clear, incremental commits (10 points)**

## Submission Guidelines

- Submit an updated link to your GitHub repository that includes:
  - Trie implementation and usage
  - Cache integration
  - Full commit history for Milestone 3

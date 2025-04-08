# CS210: Final Project Milestone 1 Requirements

In this first milestone, you will write a C++ program that reads city population data from the provided CSV file named `world_cities.csv`. The program should allow users to search for a city's population using the city name and country code. Additionally, you will implement a caching mechanism that stores the 10 most recent lookups for faster access on repeated queries. The most recent 10 cities are the only data you should store in memory for this program. 

## CSV File Format

The dataset provided contains city population records in CSV (Comma-Separated Values) format. Each row contains a country code, city name, and the population of that city. Below is a sample of the data:

```
country code,city name,population
ad,andorra la vella,20430.0
ad,canillo,3292.0
ad,encamp,11224.0
ad,la massana,7211.0
...
```

There are approximately 50,000 records in this file.

## Your Task

### 1. Read the CSV File
Write C++ code that reads the CSV file. Each time the user is prompted to enter a city name and country code, your program should:
- Open to read the file **without** loading the data onto memory.
- Search for a matching record using the entered city name and country code.
- Return and display the population for the matched city.

### 2. Implement a Cache
To improve performance for repeated searches, implement a cache that:
- Stores the 10 most recent city population lookups.
- Allows **O(1)** time lookup to check whether a city is already in the cache.
- Ensures only the **10 most recent** lookups are stored (older entries are discarded as new ones are added).

You may choose your own design for the data structure, but ensure it meets the requirements for lookup time and cache size.

### 3. User Interaction
Your program should:
- Prompt the user for a city name and country code.
- Display the population from either the cache (if present) or by reading from the CSV.
- Repeat until the user chooses to exit the program.

### 4. Testing
Test your implementation with various cities and ensure the cache updates correctly. You can use print statements or logs to verify the cache contents after each lookup.

### 5. Version Control
Use a new GitHub repository for your final project.
- Make incremental commits as you complete each feature (CSV reading, lookup logic, caching, user interface).
- Include meaningful commit messages that describe the changes you made.

## Rubric and Scoring

Your project will be graded based on the following criteria:

- **Correct CSV file reading and lookup by city and country code (25 points)**
- **Correct implementation of the caching mechanism (25 points)**
- **Proper user input handling and output display (20 points)**
- **Efficient and correct cache eviction and update strategy (20 points)**
- **Use of version control with meaningful and incremental commits (10 points)**

## Submission Guidelines

- Submit a link to your GitHub repository that contains all source code and your commit history.

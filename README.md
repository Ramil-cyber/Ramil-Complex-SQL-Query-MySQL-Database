[![CI Pipeline](https://github.com/Ramil-cyber/Ramil-Complex-SQL-Query-MySQL-Database/actions/workflows/main.yaml/badge.svg)](https://github.com/Ramil-cyber/Ramil-Complex-SQL-Query-MySQL-Database/actions/workflows/main.yaml)

# Ramil's Python Script Interacting with SQL Database

## Overview

This project demonstrates how to interact with a SQL database using Python, involving a complex SQL query that includes joins, aggregation, and sorting. The repository covers the end-to-end process, from downloading CSV files, loading them into a database, and executing queries, all while following best practices with CI/CD integration.

---

## Project Features

1. **Complex SQL Query:**
    - The project contains a SQL query that joins multiple tables, performs aggregations, and sorts the results based on the specified criteria.
  
2. **Python Integration:**
    - Python scripts are used to automate downloading CSV data from remote sources, load them into a SQL database, and execute SQL queries.

3. **CI/CD Pipeline:**
    - The project includes continuous integration and deployment (CI/CD) through GitHub Actions, ensuring the project is automatically tested upon each commit.

---

## SQL Query

The SQL query in this project involves:
- **Joins** between tables containing football club and player data.
- **Aggregation** to calculate statistics such as the average number of goals per club.
- **Sorting** to rank clubs by total goals scored.

Example Query:
```sql
Select club.name  as club_name, 
SUM(player.market_value_in_eur) as total_market_value,
COUNT(*) as included_players

from ids706_data_engineering.default.rm564_football_clubs_players player
JOIN ids706_data_engineering.default.rm564_football_clubs club ON player.current_club_id = club.club_id
GROUP BY club_name
ORDER BY total_market_value DESC
limit 20 ;
```

### Expected Results:
- **Club Name:** The name of the football club.
- **Total Market Value:** Total market value for each club.
- **Included Players:** The number of players in each club.

### Explanation:
This query joins the `rm564_football_clubs` and `rm564_football_clubs_players` tables on the `club_id`, aggregates player statistics for each club calculates the total market value and number of players included. The dataset sorted by total market value for the each club.

---

## Getting Started

### Prerequisites

- **Python 3.12**
- **Databricks Connection** (or alternative cloud SQL database)
- **GitHub Actions for CI/CD**

### Installation

1. Clone the repository:

```bash
git clone https://github.com/nogibjj/Ramil-Complex-SQL-Query-MySQL-Database.git
cd Ramil-Complex-SQL-Query-MySQL-Database
```

2. Install dependencies:

```bash
make install
```

3. Set up environment variables:

- Create a `.env` file in the root directory with the following variables:

```
SERVER_HOSTNAME=your_databricks_server_hostname
HTTP_PATH=your_http_path
ACCESS_TOKEN=your_access_token
```

### Running the Script

1. Extract CSV files and load data into the database:
   ```bash
   python main.py
   ```

2. Execute queries:
   - You can run specific SQL queries using the `execute_query` or `fetchall_result` functions.

### Running Tests

To run the tests:

```bash
make test_file
```

To run the format:

```bash
make format
```

To run the lint:

```bash
make lint
```


---

## CI/CD Pipeline

The repository uses GitHub Actions for continuous integration and deployment. Every commit triggers the CI pipeline, which:
- Runs automated tests on the Python codebase.
- Ensures the SQL query and database interactions work as expected.

### Running the Pipeline Locally

You can use GitHub Actions for CI, and Docker to replicate the CI environment locally if desired.


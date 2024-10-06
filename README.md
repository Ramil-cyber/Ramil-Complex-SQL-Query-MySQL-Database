[![CI/CD](https://github.com/nogibjj/Ramil-Python-Script-interacting-with-SQL-Database/actions/workflows/main.yaml/badge.svg)](https://github.com/nogibjj/Ramil-Python-Script-interacting-with-SQL-Database/actions/workflows/main.yaml)

# Python Script for Interacting with SQL Database

This project demonstrates how to interact with a SQL database using Python. It connects to a database, performs CRUD (Create, Read, Update, Delete) operations, and executes SQL queries. The script also integrates with a CI/CD pipeline for automated testing.

## Features
- Connects to a SQL database.
- Performs CRUD operations.
- Executes at least two SQL queries.
- Automated testing of database operations through a CI/CD pipeline.

## Project Structure
- `src/lib.py`: Python script that contain all  needed functions
- `main.py`: Python script based on the functions of the lib and perform analtyical operations
- `test_main.py`: Contains tests to validate the operations.
- `.github/workflows/`: CI/CD pipeline configuration for automated testing.

## Requirements
- Python 3.x
- SQLite3 or any SQL database
- `sqlite3` library: Comes pre-installed with Python
- `pytest` testing framework
- `black` code formatter
- `ruff`: for testing
- GitHub Actions for continuous integration and delivery (CI/CD)

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/nogibjj/Ramil-Python-Script-interacting-with-SQL-Database.git
    cd Ramil-Python-Script-interacting-with-SQL-Database
    ```
2. Install the required dependencies:
   ```
   make install
   ```
3. Format the code:
   ```
   make format
   ```
4. Lint the code:
   ```
   make lint
   ```
5. To test the scripts:
   ```
   make test_file
   ```
6. Run the Python script to connect to the SQL database and perform the operations:
   ```
   python main.py
   ```
## Database Operations
The script performs the following operations on the database:
1. **Create**: Inserts new records into the database.
2. **Read**: Queries the database and retrieves data.
3. **Update**: Updates existing records.
4. **Delete**: Removes records from the database.

### SQL Queries
The script includes at least two different SQL queries:
- Query 1: This SQL query retrieves information about the number of NBA players drafted in each year by their draft position. 
- Query 2: This SQL query retrieves the average superstar rating of players by their position and draft year, but only includes combinations where the average superstar value is greater than 0.02.

## CI/CD Pipeline
A GitHub Actions CI/CD pipeline is configured to:
- Test the database connection.
- Ensure CRUD operations work correctly.
- Validate SQL queries.

## Screenshots
### Insert Operation
![Insert Operation](https://github.com/nogibjj/Ramil-Python-Script-interacting-with-SQL-Database/blob/cdef65a8c0705cad1f2bacbf51a872c555e679ad/images/Insert_Operation.png)

---

### Analytic Query 1
![Analytic Query 1](https://github.com/nogibjj/Ramil-Python-Script-interacting-with-SQL-Database/blob/cdef65a8c0705cad1f2bacbf51a872c555e679ad/images/Analytic_Query1.png)

---

### Analytic Query 2
![Analytic Query 2](https://github.com/nogibjj/Ramil-Python-Script-interacting-with-SQL-Database/blob/cdef65a8c0705cad1f2bacbf51a872c555e679ad/images/Analtyic_Query2.png)

---

### Delete Operation
![Delete Operation](https://github.com/nogibjj/Ramil-Python-Script-interacting-with-SQL-Database/blob/cdef65a8c0705cad1f2bacbf51a872c555e679ad/images/Delete_Opertion.png)

---

### Read Operation
![Read Operation](https://github.com/nogibjj/Ramil-Python-Script-interacting-with-SQL-Database/blob/cdef65a8c0705cad1f2bacbf51a872c555e679ad/images/Read_Operation.png)

---

### Read Operation 2
![Read Operation 2](https://github.com/nogibjj/Ramil-Python-Script-interacting-with-SQL-Database/blob/cdef65a8c0705cad1f2bacbf51a872c555e679ad/images/Read_Operation2.png)

---

### Transformation (ETL)
![Transformation (ETL)](https://github.com/nogibjj/Ramil-Python-Script-interacting-with-SQL-Database/blob/cdef65a8c0705cad1f2bacbf51a872c555e679ad/images/Transformation(elt).png)

---

### Update Operation
![Update Operation](https://github.com/nogibjj/Ramil-Python-Script-interacting-with-SQL-Database/blob/cdef65a8c0705cad1f2bacbf51a872c555e679ad/images/Update_Operation.png)

---



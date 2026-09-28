# Student Records Management System

A menu-driven, command-line application written in **Python** that uses **MySQL** to create databases, define student record tables, store records, and search or display them.

---

## Table of Contents

1. [Abstract](#abstract)
2. [Objectives](#objectives)
3. [Features](#features)
4. [Tech Stack](#tech-stack)
5. [System Requirements](#system-requirements)
6. [Installation & Setup](#installation--setup)
7. [Usage](#usage)
8. [Table Formats](#table-formats)
9. [Project Structure](#project-structure)
10. [Function Reference](#function-reference)
11. [Sample Run](#sample-run)
12. [Known Limitations](#known-limitations)
13. [Future Scope](#future-scope)
14. [Conclusion](#conclusion)
15. [License](#license)

---

## Abstract

Educational institutions handle large amounts of student data such as registration numbers, names, fields of study, grades, and marks. Managing this on paper or in scattered files is slow and error-prone. This project provides a simple console-based tool that connects Python to a MySQL server so that student records can be created, stored, displayed, and searched in an organised, persistent way.

## Objectives

- Demonstrate Python–MySQL connectivity using `mysql-connector-python`.
- Let the user create databases and tables dynamically at runtime.
- Support two predefined student record formats.
- Allow insertion of multiple records in one session.
- Provide display and search operations on stored data.
- Handle common errors such as duplicate database or table names.

## Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | Create Database | Creates a new MySQL database; asks again if the name already exists |
| 2 | Create Record Table | Creates a table in one of two formats and inserts records interactively |
| 3 | Display Records | Shows all rows of a chosen table |
| 4 | Search Record | Finds a student by registration number |
| 5 | Exit | Closes the program |

Additional highlights:

- Parameterised `INSERT` queries (`%s` placeholders) for record values
- Input loop to add any number of records (`y/n`)
- Menu re-displays after each operation until the user exits

## Tech Stack

- **Language:** Python 3.x
- **Database:** MySQL 5.7 / 8.x
- **Library:** `mysql-connector-python`
- **Interface:** Command-line (CLI)

## System Requirements

- Python 3.7 or above
- MySQL Server running on `localhost`
- pip (Python package manager)

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Install the MySQL connector**
   ```bash
   pip install mysql-connector-python
   ```

3. **Start MySQL Server** and make sure you have valid credentials.

4. **Configure the connection** at the top of the script:
   ```python
   con = sql.connect(host="localhost", user="root", password="your_password")
   ```
   > Replace `your_password` with your own MySQL password. Do not commit real passwords to GitHub.

5. **Run the program**
   ```bash
   python main.py
   ```

## Usage

When the program starts, the following menu appears:

```
------Student Records------
1. Create Database
2. Creating Record Table
3. Display Record
4. Search Record
5. Exit
```

Recommended order for first-time use:

1. Choose **1** to create a database.
2. Choose **2**, enter that database name, pick a table format (`F1` or `F2`), name the table, and add records.
3. Choose **3** to view all records or **4** to search by registration number.
4. Choose **5** to exit.

## Table Formats

**Format F1 – Academic Summary**

| Column | Type |
|--------|------|
| Registration_ID | VARCHAR(50) |
| Student_Name | VARCHAR(50) |
| Field_Of_Student | VARCHAR(50) |
| Overall_Grade | VARCHAR(50) |
| CGPA | VARCHAR(50) |

**Format F2 – Marks Sheet**

| Column | Type |
|--------|------|
| Registration_ID | VARCHAR(50) |
| Student_Name | VARCHAR(50) |
| Total_Marks | INT |
| Scored_Marks | INT |

## Project Structure

```
.
├── main.py        # Complete application source code
└── README.md      # Project report / documentation
```

## Function Reference

| Function | Purpose |
|----------|---------|
| `create_database()` | Prompts for a name and runs `CREATE DATABASE`; retries on failure |
| `table()` | Selects a database, lets the user choose format F1/F2, creates the table, and inserts records in a loop |
| `display()` | Selects a database and table, then prints every record using `SELECT *` |
| `search()` | Fetches all rows of a table and prints those matching the entered registration number |
| Main loop | Displays the menu, reads the choice, and calls the matching function |

## Sample Run

```
------Student Records------
1. Create Database
2. Creating Record Table
3. Display Record
4. Search Record
5. Exit
Enter your choice: 1
Enter your database name: school
Your database has created

Enter your choice: 2
Enter your database name to be used for creating table: school
Now you are using school database
Enter your formate choice (F1 & F2): F2
Enter your table name: marks
Your table of choosen formate is created successfully
Enter student's registration number: 101
Enter student's name: Aman
Enter total marks: 500
Enter student's obtained marks: 432
Record added successfully into your selected table
Want to enter more record? (y/n) : n

Enter your choice: 3
...
('101', 'Aman', 500, 432)
```

## Known Limitations

- Database credentials are hard-coded in the source file.
- Database and table names are inserted with `str.format()`, which is not safe against SQL injection.
- Bare `except:` blocks treat every error as a "name already exists" error.
- The search reads the whole table into memory instead of using a `WHERE` clause.
- No update or delete operations.
- No primary key on `Registration_ID`, so duplicate IDs are allowed.
- CGPA is stored as text rather than a numeric type.

## Future Scope

- Add **Update** and **Delete** record options
- Make `Registration_ID` a `PRIMARY KEY`
- Use `WHERE Registration_ID = %s` for searching
- Store credentials in environment variables or a `.env` file
- Validate names and numeric input
- Export records to CSV or Excel
- Build a GUI (Tkinter) or web interface (Flask/Django)
- Add login and role-based access for staff

## Conclusion

The Student Records Management System shows how Python and MySQL can be combined to build a practical data-management tool. It covers core database operations (create, insert, select, search) in a simple interface, making it a good foundation for learning database programming and for extending into a full student information system.

## License

This project is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute it.

---

*Made with Python and MySQL.*

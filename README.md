# To-Do List Manager with MySQL

## Description
This is a simple To-Do List Manager application built using Python's Tkinter for the GUI and MySQL for data storage. It allows users to add, update, delete, and view tasks stored in a MySQL database.

## Features
- Add new tasks to the to-do list
- Update existing tasks
- Delete tasks from the list
- View all tasks in a listbox
- Display all tasks in a messagebox

## Requirements
Ensure you have the following installed on your system:
- Python (>=3.7)
- MySQL Server
- Required Python libraries:
  ```bash
  pip install mysql-connector-python
  ```

## Database Setup
Before running the application, set up your MySQL database:
1. Open MySQL and create a database:
   ```sql
   CREATE DATABASE todolist;
   ```
2. Use the database:
   ```sql
   USE todolist;
   ```
3. Create a `tasks` table:
   ```sql
   CREATE TABLE tasks (
       id INT AUTO_INCREMENT PRIMARY KEY,
       task_name VARCHAR(255) NOT NULL
   );
   ```

## Installation and Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/todo-list-mysql.git
   ```
2. Navigate to the project directory:
   ```bash
   cd todo-list-mysql
   ```
3. Run the Python script:
   ```bash
   python app.py
   ```

## Configuration
Modify the database connection details in the script to match your MySQL credentials:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this to your MySQL username
    password="yourpassword",  # Change this to your MySQL password
    database="todolist"
)
```

## Screenshots
(Include screenshots of the application if possible.)

## License
This project is licensed under the MIT License.

## Contributing
Feel free to contribute by submitting issues or pull requests to improve the functionality.


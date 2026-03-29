# Student Report System

## Description
This is a Python-based console application to manage student records.
It allows users to add, view, search, update, and delete student data.

## Features
- Add student with marks
- View all student reports
- Search student by name
- Update student marks
- Delete student record
- Prevent duplicate entries
- Calculates total, average, grade, max, and min marks
- Stores data using JSON file

## How to Run
1. Make sure Python is installed
2. Run the program:
   python main.py

## How It Works
- Data is stored in a file called `students.json`
- Each student has a name and a list of marks
- The program calculates report details dynamically

## Technologies Used
- Python
- JSON (for data storage)

## Notes
- Input validation is applied for marks
- Duplicate student names are not allowed

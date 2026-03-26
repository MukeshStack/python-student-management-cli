# 🎓 Student Management System CLI (Python - OOP)

A command-line based Student Management System built using Python.
This version is refactored using **Object-Oriented Programming (OOP)** for better structure, scalability, and maintainability.

---

## 🚀 Features

* ➕ Add student (name & marks)
* 📋 View all students
* 🔍 Search student by name (case-insensitive)
* ✏️ Update student marks (with validation)
* ❌ Delete student
* 💾 Persistent storage using file handling (`student.txt`)
* 🛡️ Input validation using `try-except`
* 🧱 OOP-based design (class & methods)
* ♻️ Centralized file saving logic

---

## 🧠 Concepts Used

* Object-Oriented Programming (Classes, Objects, Methods)
* Lists & Dictionaries (data modeling)
* Functions & Code Reusability
* Loops & Conditional Logic
* CRUD Operations
* File Handling (`read`, `write`)
* Error Handling (`try-except`)
* Data Validation (range checking)

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/MukeshStack/python-student-management-cli.git
```

2. Navigate to project folder:

```bash
cd python-student-management-cli
```

3. Run the program:

```bash
python main.py
```

---

## 📌 Example Menu

```
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Update Student
6. Exit
```

---

## 🧱 Project Structure

```
main.py
student.txt   # Stores student data
README.md
```

---

## ⚠️ Design Approach

* `self.students` is the main data source (in-memory)
* File is used only for persistence (storage)
* All operations modify memory first, then sync with file
* Avoids inconsistent data caused by mixed file operations

---

## 🚧 Future Improvements

* Build REST API using Flask
* Add database (SQLite / PostgreSQL)
* Create web interface (React / HTML-CSS)
* Add authentication system
* Logging & error tracking

---

## 👨‍💻 Author

**Mukesh Kumar**

* GitHub: https://github.com/MukeshStack
* LinkedIn: https://linkedin.com/in/mukesh-kumar-9a8311368

---

## ⭐ Note

This project reflects my transition from basic Python scripting to structured OOP-based development, with a focus on backend thinking and data consistency.

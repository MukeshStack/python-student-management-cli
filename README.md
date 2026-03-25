# 🎓 Student Management System CLI (Python)

A command-line based Student Management System built using Python.
This project performs full CRUD operations with **file persistence and input validation**, making it more robust than a basic beginner project.

---

## 🚀 Features

* ➕ Add student (name & marks)
* 📋 View all students
* 🔍 Search student by name (case-insensitive)
* ✏️ Update student marks (with validation)
* ❌ Delete student
* 💾 Persistent storage using file handling (`student.txt`)
* 🛡️ Input validation using `try-except`
* 📌 Menu-driven CLI interface
* ♻️ Reusable function for file saving (clean structure)

---

## 🧠 Concepts Used

* Lists & Dictionaries (data modeling)
* Functions & Code Reusability
* Loops & Conditional Logic
* CRUD Operations
* File Handling (`read`, `write`, `append`)
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

## ⚠️ Current Limitations

* Uses global state (`students` list)
* CLI-based (no GUI yet)
* No database (uses text file instead)

---

## 🚧 Future Improvements

* Refactor into OOP (class-based design)
* Build REST API using Flask
* Add database (SQLite / PostgreSQL)
* Create web interface (React / HTML-CSS)
* Add authentication system

---

## 👨‍💻 Author

**Mukesh Kumar**

* GitHub: https://github.com/MukeshStack
* LinkedIn: https://linkedin.com/in/mukesh-kumar-9a8311368

---

## ⭐ Note

This project reflects my progress from basic Python to structured problem-solving.
Built as part of my journey toward backend development and AI.

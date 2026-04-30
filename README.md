# 🚀 Smart Coaching Management System with Automated Scheduling

## 📌 Overview

The **Smart Coaching Management System** is a web-based application designed to manage educational institutes efficiently. It provides features like student management, course handling, and communication, along with an advanced **automated scheduling system**.

Unlike traditional systems, this project introduces a **constraint-based scheduling engine** that dynamically allocates teachers, classrooms, and time slots using optimization techniques.

---

## 🎯 Problem Statement

In coaching institutes:

* Resources (teachers, classrooms, time) are limited
* Manual scheduling causes conflicts and inefficiencies
* Proper allocation is time-consuming

### ✅ Solution

A system that:

* Automates timetable generation
* Handles constraints dynamically
* Optimizes resource utilization

---

## 🧠 Key Features

### 🔹 Core CMS Features

* Admin dashboard
* Student & course management
* Interactive UI for managing resources
* JSON-based data storage (no database required)

---

### 🔹 Automated Scheduling System (Main Feature)

* Dynamic input of:

  * Teachers
  * Rooms
  * Time slots
  * Classes
* Constraint-based allocation:

  * Room capacity validation
  * Teacher availability
  * Class compatibility rules
* Conflict detection & handling
* Generates optimized timetable automatically

---

## ⚙️ Algorithms Used

### 🔸 Greedy Algorithm

* Sorts classes by priority
* Assigns first available resources
* Ensures fast scheduling

### 🔸 Optimization Phase

* Improves initial schedule
* Reduces conflicts
* Maximizes resource utilization

### 🔸 Hybrid Approach

* Greedy → Initial allocation
* Optimization → Refinement

---

## 🏗️ Project Structure

```
project/
├── app.py
├── routes/
│   ├── auth.py
│   ├── resources.py
│   ├── schedule.py
├── services/
│   ├── scheduler.py
│   ├── json_storage.py
├── data/
│   ├── teachers.json
│   ├── rooms.json
│   ├── timeslots.json
│   ├── classes.json
│   ├── schedule.json
├── templates/
├── static/
├── utils/
└── requirements.txt
```

---

## 💾 Data Storage

* Uses **JSON files** instead of a database
* Lightweight and easy to manage
* Suitable for small to medium systems

---

## 🌐 Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, Bootstrap, JavaScript
* **Storage:** JSON
* **UI:** Responsive dashboard with modern design

---

## 📊 Sample Output

```
Class: 11
Teacher: Vikash Kumar
Room: R1
Time: 9:00 - 10:00
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/smart-coaching-management-system.git
cd smart-coaching-management-system
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the application

```
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📈 Applications

* Coaching institutes
* Schools and colleges
* Training centers
* Small educational organizations

---

## 🔥 Future Enhancements

* Database integration (PostgreSQL / MySQL)
* AI-based schedule prediction
* Multi-branch management
* Advanced analytics dashboard

---

## 🧠 Learning Outcomes

* Practical use of Greedy algorithms
* Real-world optimization problem solving
* System design and modular architecture
* Full-stack development

---

## 👨‍💻 Author

**Avinash Kumar**
B.Tech CSE Student

---

## ⭐ Contribution

Feel free to fork, improve, and contribute to this project!

---

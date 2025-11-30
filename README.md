# Coding Pasanga  
### A Learning & Skill-Building Platform for Hostel Juniors  
**Tech Stack:** Django · Tailwind CSS · JavaScript · HTML

Coding Pasanga is an interactive web platform designed to help students learn coding, track their progress, and access curated resources in DSA, Web Development, and more.  
Built using **Django**, styled with **Tailwind CSS**, and enhanced with **JavaScript**, the platform allows users to learn, practice, and monitor their daily activity.

---

## Features

### **User Authentication**
- Custom **Signup / Login / Logout** system  
- Fully customized **Password Reset flow** (`newpswd.html` styled with Tailwind)  
- Email verification support (optional)

---

### **User Profile & Account Settings**
- Editable **profile page** (Full Name, Profile Photo, LinkedIn ID, etc.)  
- Dynamic profile picture with hover effect  
- Form validation + Django messages  
- Default random avatar for new users  

---

### **Daily Progress Tracking (DSA + Website Activity)**
Coding Pasanga tracks user learning using two methods:

#### **1. LeetCode & GFG Integration**
- Users enter their usernames  
- Platform automatically fetches:
  - Daily solved problem count  
  - Submissions  
  - Streak  
- Data shown in a beautiful **calendar heatmap**

#### **2. Backup Tracking (For users without LC/GFG)**
- Django signals record:
  - Login activity  
  - Time spent on the website  
- JavaScript (`timeTracker.js`) logs user duration and stores it  
- Heatmap updates automatically  

---

### **Interactive Dashboard**
Dashboard displays:
- Daily progress heatmap  
- Weekly activity summary  
- Total time spent  
- Learning suggestions based on activity  
- Recently accessed modules  

---

### **Courses Included**
- **DSA Roadmap**
- **Web Development Roadmap**
- **Python Basics**
- **System Design (beginner friendly)**  
More courses can be added easily using modular templates.

---

## Tech Stack

| Layer | Technologies |
|------|--------------|
| Backend | Django, Django REST Framework |
| Frontend | Tailwind CSS, HTML, JavaScript |
| Database | SQLite / PostgreSQL |
| External APIs | LeetCode API, GFG API |
| Tracking | Django signals + JS time tracker |

---

## Screenshot

<p align="center">
  <img width="650" height="768" alt="Image" src="https://github.com/user-attachments/assets/cff8bdbb-9f35-4b9d-8673-e7f95bc64ca2" />
  <img width="650" height="768" alt="Image" src="https://github.com/user-attachments/assets/ab6c2c7b-2397-4843-883a-356e16a2cc40" />
</p>

<p align="center">
  <img width="650" height="768" alt="Image" src="https://github.com/user-attachments/assets/052feb76-07dc-4141-a1c1-3c9323c4472a" />
</p>




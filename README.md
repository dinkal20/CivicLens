# 🏙️ CivicFix – Civic Issue Reporting System

CivicFix is a web-based civic issue reporting and management platform that allows citizens to report public infrastructure and community-related issues. It helps streamline communication between citizens, administrators, and departments to support efficient issue management.

## ✨ Features

- **User Registration & Login:** Secure authentication for users.
- **Report Submission:** Citizens can submit reports about civic issues.
- **Location Tracking:** Capture geographical coordinates (latitude and longitude) of reported issues.
- **Report Management:** View and track submitted reports.
- **Admin Dashboard:** Manage reports and oversee platform activities.
- **Department Management:** Organize reports based on responsible departments.
- **Category Classification:** Categorize civic issues for better organization.
- **AI-Based Issue Detection:** Identify road-related damage using an AI-based detection model.
- **Report Tracking:** Monitor the status of submitted reports.

## 🛠️ Technologies Used

**Frontend:**
- HTML5
- CSS3
- JavaScript
- Leaflet.js

**Backend:**
- Python
- Flask
- Flask-CORS
- Werkzeug

**Database:**
- MongoDB Atlas
- PyMongo

**AI / Machine Learning:**
- YOLO (Object Detection)

## 📂 Project Structure

```text
CivicFix/
│
├── app.py
├── requirements.txt
├── .env
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── ...
│
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

### 2. Navigate to the Project Folder

```bash
cd CivicFix
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file and add your MongoDB connection details.

```env
MONGO_URI=your_mongodb_connection_string
```

### 6. Run the Application

```bash
python app.py
```

Open the application in your browser using the local URL displayed in the terminal.

## 🔄 How It Works

1. Citizens register and log in to the platform.
2. Citizens submit reports describing civic issues.
3. Location coordinates are associated with reports.
4. Reports are organized into relevant categories and departments.
5. Administrators manage reports and coordinate their handling.
6. Citizens can view and track their submitted reports.

## 🎯 Project Objective

The main objective of CivicFix is to provide a centralized digital platform for reporting and managing civic issues, improving communication between citizens and authorities and supporting more organized issue resolution.

## 👩‍💻 Developed By

**Dinkal Leuva**

B.Tech – Information Technology

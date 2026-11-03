#### **CivicLens**

#### 

##### **AI-Powered Civic Issue Reporting and Management System**



CivicLens is a web-based platform designed to simplify civic issue reporting and management. It enables citizens to report civic issues while allowing administrators and departments to manage, assign and track reports efficiently.



###### **Features:--**



\- **Citizen Authentication:** Secure registration and login system.

\- **AI-Based Issue Detection:** Uses an AI model to identify civic issues.

\- **Location-Based Reporting:** Allows citizens to report issues with geographical locations.

\- **Report Management:** Enables citizens to submit and track their reports.

\- **Department Management**: Organizes reports according to responsible departments.

\- **Admin Dashboard:** Provides administrative control over reports and departments.

\- **Report Tracking:** Helps monitor the progress and status of reported issues.



###### **Technologies Used:--**



\- **Programming Language:** Python

\- **Backend:** Flask

\- **Frontend:** HTML, CSS, JavaScript

\- **Database:** MongoDB Atlas

\- **AI Model:** YOLO

\- **Map Integration:** Leaflet

\- **Libraries:** Flask-CORS, PyMongo, Python-dotenv



###### **Database Structure:--**

###### 

**Database Name:** civicfix



**Collections:**

\- users

\- admin

\- departments

\- reports



###### **Project Structure:--**


CivicLens/

│

├── Backend/

│   ├── app.py

│   ├── config.py

│   ├── create\\\_admin.py

│   ├── migrate\\\_accounts.py

│   ├── best.pt

│   ├── requirements.txt

│   └── .env.example

│

├── Frontend/

│

├── docs/

│   └── screenshots/

│

├── .gitignore

└── README.md




###### **Installation and Setup:--**



**1. Clone the Repository**



```bash

git clone https://github.com/YOUR-USERNAME/CivicLens.git

cd CivicLens

```



**2. Install Dependencies**



```bash

pip install -r Backend/requirements.txt

```



**3. Configure Environment Variables**



Create a `.env` file inside the Backend folder using `.env.example` as a reference.



Configure the following variables:



\- MONGO\_URI

\- SECRET\_KEY



Use your own MongoDB connection string and secret key.



**4. Run the Application**



```bash

python Backend/app.py

```



Open the local URL displayed in the terminal to access CivicLens.



###### **Screenshots:--**

###### 

Application screenshots are available in the `docs/screenshots/` directory.



###### **Future Enhancements:--**



\- Improved AI-based civic issue classification.

\- Enhanced report analytics.

\- Real-time report tracking.

\- Improved coordination between citizens and departments.





**CivicLens – Making Civic Issue Reporting Smarter and Simpler.**



**Author**

**Dinkal Leuva**


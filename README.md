# Smart Nutritional Ration Distribution System

## Overview
The **Smart Nutritional Ration Distribution System** is a web-based platform designed to optimize the allocation of food subsidies based on individual nutritional needs. The system integrates **React, PostgreSQL, Python, Rule-Based Systems, and Case-Based Systems** to provide a data-driven approach to food distribution.

## Features

### 1. Role-Based Access Control (RBAC)
- Different user roles: **Citizens, Central Admins, Diagnostic Centers, and Ration Shops**.
- Ensures **authorization and separation of privileges** across modules.

### 2. Rule-Based Food Subsidy Allocation
- Collects **nutritional reports** from diagnostic centers.
- Uses a **rule-based system** to allocate food subsidies based on health conditions.
- Optimized **PostgreSQL queries** for efficient database performance.

### 3. Real-time Analytics Dashboard
- Tracks **citizens' health metrics and food allocation details**.
- Generates **insights and reports** for better decision-making.

### 4. Nutritional Report Management
- Stores **past nutritional reports**.
- Allows citizens to **download and view reports as PDFs**.

## Tech Stack
- **Frontend:** React.js
- **Backend:** Python
- **Database:** PostgreSQL
- **Authorization & Authentication:** Role-Based Access Control (RBAC)
- **Logic Implementation:** Rule-Based System & Case-Based System

## Installation & Setup

### Prerequisites:
- **Node.js & npm/yarn**
- **Python 3.8+**
- **PostgreSQL**

### Steps to Run:
#### Clone the Repository:
```sh
git clone https://github.com/Moni282003/Public_distribution_system.git
cd Public_distribution_system
```

#### Backend Setup:
```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python app.py
```

#### Frontend Setup:
```sh
cd frontend
npm install  # or `yarn install`
npm start  # or `yarn start`
```

## Future Enhancements
- **AI-based food recommendation** based on medical history.
- **Integration with IoT** for real-time health tracking.
- **Mobile App Version** for better accessibility.

---
**Monish M - Developer**

*Note: If you face any issues, feel free to open an issue on [GitHub](https://github.com/Moni282003/Public_distribution_system/issues).*


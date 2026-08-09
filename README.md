# 🏥 MedCare — Smart Healthcare Management Platform

> **Making healthcare smarter, faster, and more connected.**

MedCare is an **AI-powered Smart Healthcare Management Platform** designed to improve hospital operations and patient experience by bringing essential healthcare services together in one unified system.

The project addresses challenges such as **long OPD queues, unpredictable waiting times, lack of real-time bed availability, inefficient emergency coordination, and fragmented hospital information**.

Inspired by the **SIH1621 — Hospital OPD Queuing & Bed Availability Model with City-Wide Integration** problem statement, MedCare is designed as a foundation for connecting hospitals, patients, doctors, ambulance services, and healthcare administrators.

---

## 🎯 Problem

Patients often visit hospitals without knowing:

* How long the OPD queue is
* How many patients are waiting
* Whether beds are available
* Which department they should visit
* Whether emergency facilities are available

At the same time, hospitals face difficulties in managing patient flow, bed capacity, OPD queues, and emergency resources.

During emergencies, the absence of coordinated hospital information can result in patients being directed toward already crowded facilities while other hospitals may have available resources.

**MedCare aims to bridge this information and coordination gap.**

---

## 💡 Our Solution

MedCare provides a centralized digital platform that combines:

**Patient Services → OPD Management → Bed Monitoring → AI Assistance → Ambulance Coordination → Hospital Analytics**

The platform provides different functionalities for patients, doctors, hospital administrators, and future city-level healthcare authorities.

---

## ✨ Key Features

### 👤 Patient Management

* Secure user registration and login
* Role-based authentication
* Patient dashboard
* Online appointment booking
* Hospital and doctor information

### 🎫 Digital OPD Queue

* Digital token generation
* QR-code based token verification
* OPD queue management
* Department-wise queues
* Queue status monitoring
* Doctor-side queue visibility

### 🛏️ Hospital Bed Availability

* Hospital-wise bed information
* ICU bed availability
* General ward availability
* Emergency bed availability
* Total, occupied, and available bed tracking
* Bed availability status

This allows patients and emergency services to identify hospitals with available capacity.

### 🤖 AI-Powered Symptom Assessment

MedCare includes an AI-assisted symptom assessment module that:

* Accepts patient symptoms
* Performs preliminary risk assessment
* Identifies priority level
* Suggests an appropriate medical department
* Provides an initial recommendation

> **Note:** The symptom assessment is intended as decision support and does not replace professional medical diagnosis.

### 🚑 Ambulance Management

The ambulance module provides:

* Ambulance availability
* Vehicle information
* Driver information
* Current location/status
* Emergency coordination support

### 📊 Hospital Analytics

Hospital administrators can monitor:

* Patient statistics
* Appointment information
* Queue activity
* Bed utilization
* Operational information
* Healthcare resource trends

### 🌆 City-Level Healthcare Vision

MedCare is designed to evolve into a city-wide healthcare coordination platform where participating hospitals can share operational information through a centralized dashboard.

Future city-level integration can enable:

* Cross-hospital bed visibility
* Hospital load monitoring
* Capacity-aware emergency routing
* Healthcare resource allocation
* City-wide emergency response

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │       Patients       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       MedCare        │
                    │    Web Platform      │
                    └──────────┬───────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
   ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
   │ OPD & Queue │      │ AI Symptom  │      │ Bed         │
   │ Management  │      │ Assessment  │      │ Availability│
   └─────────────┘      └─────────────┘      └─────────────┘
          │                    │                    │
          └────────────────────┼────────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Hospital Database  │
                    │     SQLAlchemy       │
                    │       SQLite         │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
      ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
      │   Doctors   │   │ Administrators│  │  Ambulances │
      └─────────────┘   └─────────────┘   └─────────────┘
```

---

## 🛠️ Technology Stack

### Backend

* **Python**
* **Flask**
* **Flask-Login**
* **SQLAlchemy**
* **SQLite**

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript**
* **Bootstrap**
* **Font Awesome**

### AI

* AI-driven symptom analysis
* Risk-level classification
* Department recommendation
* Emergency priority assessment

### Database

The project currently uses **SQLite** with SQLAlchemy ORM.

Main database models include:

* `User`
* `Doctor`
* `Appointment`
* `QueueToken`
* `BedAvailability`
* `Ambulance`
* `EmergencyAssessment`

---

## 📂 Project Structure

```text
MedCare/
│
├── app.py
├── models.py
├── medcare.db
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── appointment.html
│   ├── queue.html
│   ├── beds.html
│   ├── doctors.html
│   ├── ambulance.html
│   ├── symptom_checker.html
│   ├── doctor_dashboard.html
│   ├── hospital_dashboard.html
│   └── city_dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── qr/
│
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/bhumiika05/MedCare-Hospital-System.git
```

### 2. Navigate to the project

```bash
cd MedCare-Hospital-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

The application will be available locally at:

```text
http://127.0.0.1:5000
```

---

## 🌐 Deployment

MedCare can be deployed as a Flask web application using platforms such as **Render**.

The production application uses Gunicorn:

```bash
gunicorn app:app
```

The project is structured so that the SQLite database can be replaced with a cloud database such as PostgreSQL when scaling to production.

---

## 🎯 Target Users

MedCare is designed for:

* 👨‍👩‍👧 Patients and caregivers
* 👨‍⚕️ Doctors
* 🏥 Hospital administrators
* 🚑 Ambulance and emergency services
* 🏛️ Healthcare authorities
* 🌆 Future city-wide healthcare networks

---

## 🌍 Social Impact

MedCare aims to:

* Reduce unnecessary hospital waiting
* Improve OPD queue transparency
* Improve hospital bed utilization
* Support faster emergency coordination
* Reduce unnecessary patient travel
* Help hospitals manage patient load
* Support data-driven healthcare decisions
* Improve accessibility to healthcare information

### Our Vision

> **Every patient informed. Every hospital connected. Every minute matters.**

---

## 🔮 Future Scope

MedCare can be expanded with:

### 🤖 Predictive Analytics

Machine-learning models can forecast:

* OPD waiting times
* Patient arrival patterns
* Hospital crowding
* Bed demand

### 🗺️ Smart Emergency Routing

GIS integration can recommend hospitals based on:

* Distance
* Available beds
* Emergency capacity
* Traffic conditions
* Hospital workload

### ☁️ Cloud Infrastructure

The SQLite database can be migrated to:

* PostgreSQL
* Cloud-hosted databases
* Distributed healthcare infrastructure

### 🔗 Healthcare API Integration

Future versions can integrate with:

* Hospital information systems
* Live hospital APIs
* ABDM ecosystem
* ABHA-based healthcare services

### 📱 Mobile Application

A dedicated Android/iOS application can provide patients with:

* Live queues
* Appointments
* Bed availability
* Emergency services
* Notifications

### 🌆 City-Wide Integration

The long-term vision is to connect participating hospitals into a unified healthcare network, providing authorities with a real-time overview of healthcare capacity across the city.

---

## 🔐 Security & Privacy

Future production deployment should implement:

* Strong authentication
* Role-based authorization
* Encrypted communication
* Secure API authentication
* Healthcare data encryption
* Audit logging
* Privacy-compliant data handling

The current project is an **MVP/prototype** and should not be used as a substitute for professional medical diagnosis or as a production healthcare system without appropriate clinical, security, privacy, and regulatory validation.

---

## 📌 Project Status

**Current Status: MVP / Hackathon Prototype**

Implemented modules include:

* ✅ User authentication
* ✅ Role-based access
* ✅ Appointment booking
* ✅ OPD queue management
* ✅ QR token generation
* ✅ Hospital bed availability
* ✅ Ambulance management
* ✅ AI symptom assessment
* ✅ Doctor dashboard
* ✅ Hospital dashboard
* ✅ City dashboard
* ✅ Analytics
* ✅ Responsive UI
* ✅ Deployment-ready Flask architecture

---

## 💡 Innovation

MedCare's key innovation is its **integrated approach**.

Instead of treating appointments, queues, beds, emergency assessment, ambulances, and analytics as separate systems, MedCare brings them together into one healthcare management ecosystem.

This creates a foundation for moving from **hospital-level management to city-level healthcare coordination**.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

```bash
git fork
git clone
git checkout -b feature/your-feature
git add .
git commit -m "Add your feature"
git push
```

Then open a Pull Request.

---

## 📄 License

This project is currently intended for **educational, hackathon, and prototype purposes**.

A formal open-source license can be added if the project is released for public contribution.

---

## 👩‍💻 Team

**MedCare Team**

Built with the vision of creating a smarter, faster, and more connected healthcare ecosystem.

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ and sharing your feedback.

> **MedCare — Technology that connects care, capacity, and people.**

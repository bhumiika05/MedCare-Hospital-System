from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


db = SQLAlchemy()



# ==========================
# USER
# ==========================

class User(UserMixin, db.Model):

    __tablename__ = "users"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    fullname = db.Column(
        db.String(100),
        nullable=False
    )


    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )


    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )


    role = db.Column(
        db.String(50),
        nullable=False,
        default="Patient"
    )


    phone = db.Column(
        db.String(20)
    )


    password_hash = db.Column(
        db.String(255),
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    def set_password(self,password):

        self.password_hash = generate_password_hash(password)



    def check_password(self,password):

        return check_password_hash(
            self.password_hash,
            password
        )





# ==========================
# DOCTOR
# ==========================

class Doctor(db.Model):

    __tablename__="doctors"


    id=db.Column(
        db.Integer,
        primary_key=True
    )


    name=db.Column(
        db.String(100),
        nullable=False
    )


    specialization=db.Column(
        db.String(100)
    )


    experience=db.Column(
        db.Integer
    )


    qualification=db.Column(
        db.String(120)
    )


    hospital=db.Column(
        db.String(120)
    )


    available=db.Column(
        db.Boolean,
        default=True
    )


    image=db.Column(
        db.String(200)
    )


    created_at=db.Column(
        db.DateTime,
        default=datetime.utcnow
    )





# ==========================
# APPOINTMENT
# ==========================

class Appointment(db.Model):

    __tablename__="appointments"


    id=db.Column(
        db.Integer,
        primary_key=True
    )


    patient_name=db.Column(
        db.String(100),
        nullable=False
    )


    phone=db.Column(
        db.String(20)
    )


    doctor=db.Column(
        db.String(100)
    )


    hospital=db.Column(
        db.String(100)
    )


    appointment_date=db.Column(
        db.String(50)
    )


    status=db.Column(
        db.String(30),
        default="Pending"
    )


    created_at=db.Column(
        db.DateTime,
        default=datetime.utcnow
    )





# ==========================
# QUEUE TOKEN
# ==========================

class QueueToken(db.Model):

    __tablename__ = "queue_tokens"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    patient_name = db.Column(
        db.String(100),
        nullable=False
    )


    phone = db.Column(
        db.String(20)
    )


    department = db.Column(
        db.String(100)
    )


    token_number = db.Column(
        db.Integer,
        nullable=False
    )


    status = db.Column(
        db.String(30),
        default="Waiting"
    )


    qr_code = db.Column(
    db.String(255)
    )

    completed_at = db.Column(
        db.DateTime
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    def __repr__(self):

        return f"<QueueToken {self.token_number}>"




# ==========================
# BED AVAILABILITY
# ==========================

class BedAvailability(db.Model):

    __tablename__ = "beds"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    hospital = db.Column(
        db.String(120),
        nullable=False
    )

    ward = db.Column(
        db.String(100),
        nullable=False
    )

    total_beds = db.Column(
        db.Integer,
        default=0
    )

    occupied_beds = db.Column(
        db.Integer,
        default=0
    )

    available_beds = db.Column(
        db.Integer,
        default=0
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    def __repr__(self):

        return f"<Bed {self.hospital} - {self.ward}>"





# ==========================
# AMBULANCE
# ==========================

class Ambulance(db.Model):

    __tablename__="ambulances"


    id=db.Column(
        db.Integer,
        primary_key=True
    )


    vehicle_number=db.Column(
        db.String(50)
    )


    driver_name=db.Column(
        db.String(100)
    )


    phone=db.Column(
        db.String(20)
    )


    location=db.Column(
        db.String(100)
    )


    status=db.Column(
        db.String(50),
        default="Available"
    )


    created_at=db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

# ==============================
# EMERGENCY ASSESSMENT
# ==============================

class EmergencyAssessment(db.Model):

    __tablename__ = "emergency_assessments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    patient_name = db.Column(
        db.String(100),
        nullable=False
    )

    symptoms = db.Column(
        db.Text,
        nullable=False
    )

    risk_level = db.Column(
        db.String(50)
    )

    department = db.Column(
        db.String(100)
    )

    priority = db.Column(
        db.String(50)
    )

    recommendation = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
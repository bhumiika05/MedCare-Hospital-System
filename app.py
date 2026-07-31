import qrcode
import os

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user
)

from models import (
    db,
    User,
    Appointment,
    QueueToken,
    Doctor,
    BedAvailability,
    Ambulance,
    EmergencyAssessment
)

app = Flask(__name__)

app.secret_key = "medcare_secret_key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///medcare.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():

    db.create_all()

    if BedAvailability.query.count() == 0:

        beds = [
            BedAvailability(
                hospital="AIIMS Delhi",
                ward="ICU",
                total_beds=50,
                occupied_beds=35,
                available_beds=15
            ),

            BedAvailability(
                hospital="Fortis Hospital",
                ward="General Ward",
                total_beds=100,
                occupied_beds=70,
                available_beds=30
            ),

            BedAvailability(
                hospital="Apollo Hospital",
                ward="Emergency",
                total_beds=80,
                occupied_beds=50,
                available_beds=30
            )
        ]


        db.session.add_all(beds)

        db.session.commit() 
        
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()

# ==============================
# AI SYMPTOM ANALYSIS
# ==============================

def analyze_symptoms(symptoms):


    symptoms = symptoms.lower()


    risk = "LOW"

    department = "General Medicine"

    priority = "Normal"

    recommendation = (
        "Consult a doctor for further evaluation."
    )


    emergency_words = [

        "chest pain",
        "breathing difficulty",
        "unconscious",
        "stroke",
        "severe bleeding",
        "heart attack"

    ]


    if any(
        word in symptoms
        for word in emergency_words
    ):


        risk = "HIGH"

        priority = "Emergency"


        recommendation = (
            "Immediate medical attention required."
        )



    elif (
        "fever" in symptoms
        or
        "cold" in symptoms
        or
        "cough" in symptoms
    ):


        risk = "MEDIUM"

        department = "General Medicine"

        recommendation = (
            "Schedule a doctor consultation."
        )



    if (
        "heart" in symptoms
        or
        "chest" in symptoms
    ):


        department = "Cardiology"



    elif (
        "bone" in symptoms
        or
        "fracture" in symptoms
    ):


        department = "Orthopedics"



    elif (
        "brain" in symptoms
        or
        "head" in symptoms
    ):


        department = "Neurology"



    return (

        risk,

        department,

        priority,

        recommendation

    )

# ===================================================
# HOME
# ===================================================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/patient-dashboard")
def patient_dashboard():

    appointment = Appointment.query.order_by(
        Appointment.id.desc()
    ).first()

    token = QueueToken.query.order_by(
        QueueToken.id.desc()
    ).first()

    assessment = EmergencyAssessment.query.order_by(
        EmergencyAssessment.id.desc()
    ).first()

    return render_template(
        "patient_dashboard.html",
        appointment=appointment,
        token=token,
        assessment=assessment
    )

# ===================================================
# REGISTER
# ===================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        user = User(
            fullname=request.form["fullname"],
            username=request.form["username"],
            email=request.form["email"],
            phone=request.form["phone"],
            role=request.form["role"]
        )

        user.set_password(request.form["password"])

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


# ===================================================
# LOGIN
# ===================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()


        if user and user.check_password(password):

            login_user(user)


            role = user.role.lower().strip()


            if "doctor" in role:

                return redirect("/doctor-dashboard")


            elif "hospital" in role:

                return redirect("/hospital-dashboard")


            elif "city" in role:

                return redirect("/city-dashboard")


            else:

                return redirect("/patient-dashboard")


        return render_template(
            "login.html",
            error="Invalid Email or Password"
        )


    return render_template("login.html")


# ===================================================
# LOGOUT
# ===================================================

@app.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect("/")


# ===================================================
# APPOINTMENT BOOKING
# ===================================================

@app.route("/appointment", methods=["GET", "POST"])
def appointment():

    if request.method == "POST":

        appointment = Appointment(

            patient_name=request.form["name"],

            phone=request.form["phone"],

            doctor=request.form["doctor"],

            hospital=request.form["hospital"],

            appointment_date=request.form["date"],

            status="Pending"

        )

        db.session.add(appointment)

        db.session.commit()


        return render_template(
            "success.html",
            message="Appointment booked successfully"
        )


    return render_template("appointment.html")



# ===================================================
# QUEUE SYSTEM
# ===================================================

@app.route("/queue", methods=["GET", "POST"])
def queue():

    if request.method == "POST":

        last_token = QueueToken.query.count() + 1


        token = QueueToken(

            patient_name=request.form["name"],

            phone=request.form["phone"],

            department=request.form["department"],

            token_number=last_token,

            status="Waiting"

        )


        db.session.add(token)

        db.session.commit()



        qr_data = f"""
        MedCare OPD Token

        Token Number:
        {last_token}

        Patient:
        {token.patient_name}

        Department:
        {token.department}

        Status:
        Waiting
        """



        qr = qrcode.make(qr_data)



        filename = f"token_{last_token}.png"



        os.makedirs(
            "static/qr",
            exist_ok=True
        )



        filepath = os.path.join(
            "static",
            "qr",
            filename
        )



        qr.save(filepath)



        token.qr_code = filename


        db.session.commit()



        return render_template(

            "token_success.html",

            token=token

        )



    current_token = QueueToken.query.filter_by(

        status="Serving"

    ).first()



    waiting_count = QueueToken.query.filter_by(

        status="Waiting"

    ).count()



    return render_template(

        "queue.html",

        current_token=current_token,

        waiting_count=waiting_count

    )


# ===================================================
# SUCCESS PAGE
# ===================================================

@app.route("/success")
def success():

    return render_template(

        "success.html",

        message="Action completed successfully"

    )



# ===================================================
# DOCTOR LIST
# ===================================================

@app.route("/doctors")
def doctors():

    doctors = Doctor.query.all()


    return render_template(

        "doctors.html",

        doctors=doctors

    )



# ===================================================
# BED AVAILABILITY
# ===================================================

@app.route('/beds')
def beds():

    beds = BedAvailability.query.all()

    return render_template(
        "beds.html",
        beds=beds
    )

@app.route('/add-demo-beds')
def add_demo_beds():

    from models import BedAvailability


    demo_beds = [

        BedAvailability(
            hospital="AIIMS Delhi",
            ward="ICU",
            total_beds=50,
            occupied_beds=35,
            available_beds=15
        ),


        BedAvailability(
            hospital="AIIMS Delhi",
            ward="Emergency",
            total_beds=80,
            occupied_beds=60,
            available_beds=20
        ),


        BedAvailability(
            hospital="Safdarjung Hospital",
            ward="General Ward",
            total_beds=150,
            occupied_beds=120,
            available_beds=30
        ),


        BedAvailability(
            hospital="Max Healthcare",
            ward="Private Room",
            total_beds=100,
            occupied_beds=75,
            available_beds=25
        ),


        BedAvailability(
            hospital="Fortis Hospital",
            ward="ICU",
            total_beds=40,
            occupied_beds=40,
            available_beds=0
        )

    ]


    db.session.add_all(demo_beds)

    db.session.commit()


    return "Demo Beds Added Successfully"

# ===================================================
# AMBULANCE
# ===================================================

@app.route("/ambulance")
def ambulance():

    ambulances = Ambulance.query.all()


    return render_template(

        "ambulance.html",

        ambulances=ambulances

    )



# ==============================
# AI SYMPTOM CHECKER
# ==============================


@app.route(
    "/symptom-checker",
    methods=["GET","POST"]
)

def symptom_checker():


    result = None


    if request.method=="POST":


        name = request.form["name"]


        symptoms = request.form["symptoms"]



        risk, department, priority, recommendation = analyze_symptoms(
            symptoms
        )



        assessment = EmergencyAssessment(


            patient_name=name,


            symptoms=symptoms,


            risk_level=risk,


            department=department,


            priority=priority,


            recommendation=recommendation

        )


        db.session.add(
            assessment
        )


        db.session.commit()



        result = {


            "risk":risk,


            "department":department,


            "priority":priority,


            "recommendation":recommendation

        }



    return render_template(

        "symptom_checker.html",

        result=result

    )



# ===================================================
# DOCTOR DASHBOARD
# ===================================================

@app.route("/doctor-dashboard")
def doctor_dashboard():

    appointments = Appointment.query.all()

    queue = QueueToken.query.order_by(
        QueueToken.token_number
    ).all()

    total_patients = len(queue)

    waiting_patients = QueueToken.query.filter_by(
        status="Waiting"
    ).count()

    serving_patient = QueueToken.query.filter_by(
        status="Serving"
    ).first()

    return render_template(
        "doctor_dashboard.html",
        appointments=appointments,
        queue=queue,
        total_patients=total_patients,
        waiting_patients=waiting_patients,
        serving_patient=serving_patient
    )



# ===================================================
# HOSPITAL DASHBOARD
# ===================================================

@app.route("/hospital-dashboard")
def hospital_dashboard():

    beds = BedAvailability.query.all()

    queue = QueueToken.query.order_by(
        QueueToken.token_number
    ).all()


    total_beds = sum(
        bed.total_beds or 0
        for bed in beds
    )

    occupied = sum(
        bed.occupied_beds or 0
        for bed in beds
    )

    available = total_beds - occupied


    waiting_patients = QueueToken.query.filter_by(
        status="Waiting"
    ).count()


    return render_template(
        "hospital_dashboard.html",
        beds=beds,
        queue=queue,
        total_beds=total_beds,
        occupied=occupied,
        available=available,
        waiting_patients=waiting_patients
    )



# ===================================================
# CITY DASHBOARD
# ===================================================

@app.route("/city-dashboard")
def city_dashboard():

    patients = QueueToken.query.count()

    hospitals = BedAvailability.query.count()

    doctors = Doctor.query.count()

    ambulances = Ambulance.query.count()


    return render_template(
        "city_dashboard.html",
        patients=patients,
        hospitals=hospitals,
        doctors=doctors,
        ambulances=ambulances
    )

# ======================================
# LIVE QUEUE MANAGEMENT
# ======================================


@app.route("/call-next")
def call_next():


    current = QueueToken.query.filter_by(
        status="Serving"
    ).first()


    if current:

        current.status="Completed"

        current.completed_at=datetime.utcnow()



    next_patient = QueueToken.query.filter_by(
        status="Waiting"
    ).order_by(
        QueueToken.token_number
    ).first()



    if next_patient:

        next_patient.status="Serving"



    db.session.commit()



    return redirect("/doctor-dashboard")






@app.route("/complete-patient/<int:id>")
def complete_patient(id):


    patient = QueueToken.query.get(id)


    if patient:


        patient.status="Completed"

        patient.completed_at=datetime.utcnow()


        db.session.commit()



    return redirect("/doctor-dashboard")

# ===================================================
# AI HEALTHCARE ANALYTICS DASHBOARD
# ===================================================


@app.route("/analytics")
def analytics():


    total_appointments = Appointment.query.count()


    total_patients = QueueToken.query.count()


    emergency_cases = EmergencyAssessment.query.count()



    high_risk_cases = EmergencyAssessment.query.filter_by(
        risk_level="HIGH"
    ).count()



    medium_risk_cases = EmergencyAssessment.query.filter_by(
        risk_level="MEDIUM"
    ).count()



    low_risk_cases = EmergencyAssessment.query.filter_by(
        risk_level="LOW"
    ).count()



    doctors_count = Doctor.query.count()



    hospitals_count = BedAvailability.query.count()



    ambulance_count = Ambulance.query.count()





    # Department analysis


    cardiology = QueueToken.query.filter_by(
        department="Cardiology"
    ).count()



    general = QueueToken.query.filter_by(
        department="General Medicine"
    ).count()



    neurology = QueueToken.query.filter_by(
        department="Neurology"
    ).count()



    orthopedics = QueueToken.query.filter_by(
        department="Orthopedics"
    ).count()





    return render_template(

        "analytics.html",

        total_appointments=total_appointments,

        total_patients=total_patients,

        emergency_cases=emergency_cases,

        high_risk_cases=high_risk_cases,

        medium_risk_cases=medium_risk_cases,

        low_risk_cases=low_risk_cases,

        doctors_count=doctors_count,

        hospitals_count=hospitals_count,

        ambulance_count=ambulance_count,


        cardiology=cardiology,

        general=general,

        neurology=neurology,

        orthopedics=orthopedics

    )
# ===================================================
# AI HOSPITAL RECOMMENDATION SYSTEM
# ===================================================

@app.route("/recommendation", methods=["GET", "POST"])
def recommendation():

    result = None


    if request.method == "POST":


        name = request.form["name"]

        symptoms = request.form["symptoms"]



        risk, department, priority, advice = analyze_symptoms(
            symptoms
        )



        hospital = BedAvailability.query.order_by(
            BedAvailability.available_beds.desc()
        ).first()



        if hospital:

            hospital_name = hospital.hospital
            beds = hospital.available_beds

        else:

            hospital_name = "No hospital data available"
            beds = 0




        waiting_patients = QueueToken.query.filter_by(
            department=department,
            status="Waiting"
        ).count()



        result = {

            "name": name,

            "risk": risk,

            "department": department,

            "priority": priority,

            "advice": advice,

            "hospital": hospital_name,

            "beds": beds,

            "waiting": waiting_patients * 10

        }



    return render_template(
        "recommendation.html",
        result=result
    )
# ===================================================
# RUN APPLICATION
# ===================================================

if __name__ == "__main__":

    app.run(

        debug=True

    )

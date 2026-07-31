from app import app
from models import db, BedAvailability



with app.app_context():


    hospital1 = BedAvailability(

        hospital_name="AIIMS Delhi",

        city="Delhi",

        total_beds=2500,

        available_beds=420,

        emergency_beds=35

    )



    hospital2 = BedAvailability(

        hospital_name="Safdarjung Hospital",

        city="Delhi",

        total_beds=1800,

        available_beds=210,

        emergency_beds=20

    )



    hospital3 = BedAvailability(

        hospital_name="Max Hospital",

        city="Delhi",

        total_beds=700,

        available_beds=85,

        emergency_beds=10

    )



    db.session.add_all(
        [
            hospital1,
            hospital2,
            hospital3
        ]
    )


    db.session.commit()


print("Hospital data added")
# import necessary libraries
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy

# DATABASE_URL is automatically populated from Heroku
# Removed SQLite connection as this example connects to postgres
# .replace("://", "ql://", 1) addresses Heroku dialect mismatch
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace("://", "ql://", 1)

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Combined_table = create_classes(db)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# @TODO: Route needed for each dataset
# Example 1: Two column table
@app.route("/api/crime.json")
def crime():
    results = db.session.query(Combined_table.state, Combined_table.Solved, Combined_table.Year).all()
    #Combined_table.CNTYFIPS, Combined_table.Month, Combined_table.Incident, Combined_table.Homicide, Combined_table.VicAge, Combined_table.VicRace, Combined_table.OffAge, Combined_table.OffSex, Combined_table.Weapon, Combined_table.Relationship, Combined_table.VicCount, Combined_table.OffCount, Combined_table.latitude, Combined_table.longitude, Combined_table.name).all()

    state_text = [result[0] for result in results]
    Solved = [result[1] for result in results]
    Year = [result[2] for result in results]
    # CNTYFIPS=[result[3] for result in results]
    # Month=[result[3] for result in results]
    # Incident=[result[4] for result in results]
    # Homicide=[result[5] for result in results]
    # VicAge=[result[6] for result in results]
    # VicRace=[result[7] for result in results]
    # OffAge=[result[8] for result in results]
    # OffSex=[result[9] for result in results]
    # Weapon=[result[10] for result in results]
    # Relationship=[result[11] for result in results]
    # VicCount=[result[12] for result in results]
    # OffCount=[result[13] for result in results]
    # latitude=[result[14] for result in results]
    # longitude=[result[15] for result in results]
    # name=[result[16] for result in results]

    crime_data = [{
        "state": state_text,
        "Solved": Solved,
        "Year": Year
        # "CNTYFIPS":CNTYFIPS,
        # "Month": Month,
        # "Incident": Incident,
        # "Homicide": Homicide,
        # "VicAge": VicAge,
        # "VicRace":VicRace,
        # "OffAge": OffAge,
        # "OffSex": OffSex,
        # "Weapon":Weapon,
        # "Relationship": Relationship,
        # "VicCount":VicCount,
        # "OffCount": OffCount,
        # "latitude": latitude,
        # "longitude":longitude,
        # "name":name
    }]

    return jsonify(crime_data)

if __name__ == "__main__":
    app.run()

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
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://wgnfpbzkibzvqz:977eb8f2aac5267b997983b11d4ea7e1b477b48e8a8c94e3737c134e4b3904ac@ec2-52-6-211-59.compute-1.amazonaws.com:5432/d1kan62k27bpv5"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace("://", "ql://", 1)

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Combined_table = create_classes(db)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Example 1: Two column table
@app.route("/api/crime.json")
def crime():
    #results = db.session.query(Combined_table.State, Combined_table.CNTYFIPS, Combined_table.Solved, Combined_table.Year, Combined_table.Month, Combined_table.Incident, Combined_table.Homicide, Combined_table.VicAge, Combined_table.VicRace, Combined_table.OffAge, Combined_table.OffSex, Combined_table.Weapon, Combined_table.Relationship, Combined_table.VicCount, Combined_table.OffCount, Combined_table.latitude, Combined_table.longitude, Combined_table.name).all()
    results = db.session.query(Combined_table).all()
    
    all_crimes=[]
    for result in results:
        crime_data={}
        crime_data["State"]=result.State
        crime_data["CNTYFIPS"]=result.CNTYFIPS
        crime_data["Solved"]=result.Solved
        crime_data["Year"]=result.Year
        crime_data["Month"]=result.Month
        crime_data["Incident"]=result.Incident
        crime_data["Homicide"]=result.Homicide
        crime_data["VicAge"]=result.VicAge
        crime_data["VicRace"]=result.VicRace
        crime_data["OffAge"]=result.OffAge
        crime_data["OffSex"]=result.OffSex
        crime_data["Weapon"]=result.Weapon
        crime_data["Relationship"]=result.Relationship
        crime_data["VicCount"]=result.VicCount
        crime_data["OffCount"]=result.OffCount
        crime_data["latitude"]=result.latitude
        crime_data["longitude"]=result.longitude
        crime_data["name"]=result.name

        all_crimes.append(crime_data)

    crime_data_json={"crimes": all_crimes}

    # State = [result[0] for result in results]
    # CNTYFIPS=[result[1] for result in results]
    # Solved = [result[2] for result in results]
    # Year = [result[3] for result in results]
    # Month=[result[4] for result in results]
    # Incident=[result[5] for result in results]
    # Homicide=[result[6] for result in results]
    # VicAge=[result[7] for result in results]
    # VicRace=[result[8] for result in results]
    # OffAge=[result[9] for result in results]
    # OffSex=[result[10] for result in results]
    # Weapon=[result[11] for result in results]
    # Relationship=[result[12] for result in results]
    # VicCount=[result[13] for result in results]
    # OffCount=[result[14] for result in results]
    # latitude=[result[15] for result in results]
    # longitude=[result[16] for result in results]
    # name=[result[17] for result in results]

    # crime_data = [{
    #     "state": State,
    #     "CNTYFIPS":CNTYFIPS,
    #     "Solved": Solved,
    #     "Year": Year,
    #     "Month": Month,
    #     "Incident": Incident,
    #     "Homicide": Homicide,
    #     "VicAge": VicAge,
    #     "VicRace":VicRace,
    #     "OffAge": OffAge,
    #     "OffSex": OffSex,
    #     "Weapon":Weapon,
    #     "Relationship": Relationship,
    #     "VicCount":VicCount,
    #     "OffCount": OffCount,
    #     "latitude": latitude,
    #     "longitude":longitude,
    #     "name":name
    # }]

    return jsonify(crime_data_json)

# create route that renders Barchart.html
@app.route("/BarChart/")
def bar():
    return render_template("BarChart.html")


# create route that renders map.html
@app.route("/map/")
def map():
    return render_template("map.html")


# create route that renders Resources.html
@app.route("/Resources/")
def resource():
    return render_template("Resources.html")


# create route that renders WeaponPie.html
@app.route("/WeaponPie/")
def pie():
    return render_template("WeaponPie.html")

# @TODO: Route needed for each dataset


if __name__ == "__main__":
    app.run()

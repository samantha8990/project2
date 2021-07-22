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

    state_text = [result[0] for result in results]
    Solved = [result[1] for result in results]
    Year = [result[2] for result in results]

    crime_data = [{
        "state": state_text,
        "Solved": Solved,
        "Year": Year
    }]

    return jsonify(crime_data)

if __name__ == "__main__":
    app.run()

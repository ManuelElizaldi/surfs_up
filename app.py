import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Access the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

# Preparing - reflecting tables
Base = automap_base()
Base.prepare(engine, reflect = True)

# Saving variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Creating a session link from Python to ourdatabase
session = Session(engine)

# Setting up flask. Defining our flask app called "app"
# all routes must be below this code.
app = Flask(__name__)

# Starting route
# /api/v1.0 means frist version of the app
# possible routes inside f strings
# Welcome route defined by a function:
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes: \n
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Setting up a route for precipitation
# Adding a line of code that calculates the date one year ago from the most recent date in the database
# Query is written to get the date and precipitation for the previous year
# In queries .\ means new line
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
     filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# To unravel our results we will use the function np.ravel() with results as our parameter, but first we need to convert the results into a list
# stations = stations will give us a json file that looks like --> stations = station name. It's required for the format of a list.
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


# Temperature route
# We are using the same dates and filters as previous
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# Route for statistics report
# For this we need a starting and ending date with its own parameters
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
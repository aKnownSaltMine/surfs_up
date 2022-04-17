# importing analysis dependencies
import datetime as dt
import numpy as np
import pandas as pd
# importing sqlite dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import flask dependencies
from flask import Flask, jsonify

# Setting up the database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflecting database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# saving references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# creating a session link
session = Session(engine)

# setting up flask
app = Flask(__name__)

# creating the welcome route
@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!</br>
    Available Routes:</br>
    /api/v1.0/precipitation</br>
    /api/v1.0/stations</br>
    /api/v1.0/tobs</br>
    /api/v1.0/temp/start/end</br>
    ''')

# precipitation route
@app.route('/api/v1.0/precipitation')

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# stations route
@app.route('/api/v1.0/stations')

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# creating the tobs route
@app.route('/api/v1.0/tobs')

def temp_monthly():
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Creating the temp route
@app.route('/api/v1.0/temp/<start>')
@app.route('/api/v1.0/temp/<start>/<end>')

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    
    temps = list(np.ravel(results))

    return jsonify(temps)

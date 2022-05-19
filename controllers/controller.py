from flask import render_template, request
from app import app
from models.List_of_events import *
from models.event import Event

@app.route("/events")
def index():
    return render_template('index.html', title="All Events", events = event_list)

@app.route("/events", methods=['POST'])
def create_event():
    event_title= request.form['title']
    event_date= request.form['date']
    event_location = request.form['location']
    event_description = request.form['description']
    event_guests = request.form['guests']
    new_event = Event(event_date, event_title, event_guests, event_location, event_description)
    add_event(new_event)

    return render_template('index.html', title='all events', events = event_list)



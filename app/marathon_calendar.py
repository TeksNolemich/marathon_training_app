
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from app.db import get_all_runs
from app.utils import get_week_workout_as_dict
import app.models as Models

marathon_calendar = Blueprint("marathon_calendar", __name__)


@marathon_calendar.route('/home')
@marathon_calendar.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        mileage = int(request.form['mileage'])
        runs = get_all_runs(mileage)
        return render_template('marathon_calendar/index.html', runs=runs, mileage=mileage)
    return render_template('home.html')

@marathon_calendar.route("/get_workout", methods=["GET"])
def get_workout():
    # workoutForWeek = get_workout_for_week(20, quality_1, quality_two)
    weekWorkOutWithQualitySessions = Models.WeekWorkOutWithQualitySessions(40, 13, 11)#Models.WeekWorkout(40)
    runs = weekWorkOutWithQualitySessions.get_workout_for_week()
    runs_for_week = get_week_workout_as_dict(runs)
    return render_template('marathon_workout_week/index.html', runs_for_week=runs_for_week)
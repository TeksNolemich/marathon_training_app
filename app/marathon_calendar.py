
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from app.db import get_all_runs

marathon_calendar = Blueprint("marathon_calendar", __name__)


@marathon_calendar.route('/home')
@marathon_calendar.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        mileage = int(request.form['mileage'])
        runs = get_all_runs(mileage)
        return render_template('marathon_calendar/index.html', runs=runs, mileage=mileage)
    return render_template('home.html')
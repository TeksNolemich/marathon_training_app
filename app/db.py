from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy
from flask import current_app, g
from app.utils import round_weekly_mileage

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db
    return db

db = LocalProxy(get_db)

def get_all_runs(mileage: int):
    # TODO: set mileage Rounding to enum
    mileage = round_weekly_mileage(mileage)
    try:
        return list(db.Run_Regimen.find({"Weekly_Mileage_Max": mileage}).sort('Week', -1))
    except Exception as e:
        return e
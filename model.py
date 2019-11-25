from app import db

class Data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    topic = db.Column(db.String(50))
    value = db.Column(db.Float)
    date = db.Column(db.String(15))
    time = db.Column(db.String(15))
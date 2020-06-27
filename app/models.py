from app import db, mm
from datetime import datetime


class Markers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Numeric(10,6))
    lng = db.Column(db.Numeric(10,6))
    txt = db.Column(db.String(64))
    marker_type = db.Column(db.Integer)
    updated = db.Column(db.DateTime)
    expires = db.Column(db.DateTime)
    content = db.relationship('Content', backref='place', lazy='dynamic')


class Content(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    url  = db.Column(db.String(64))
    txt  = db.Column(db.String(64))
    content_type = db.Column(db.Integer)
    updated = db.Column(db.DateTime)
    expires = db.Column(db.DateTime)
    marker_id = db.Column(db.Integer, db.ForeignKey('markers.id'))

class Feedback(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    contact = db.Column(db.String(32))
    copyright = db.Column(db.Boolean(), nullable=True)
    privacy = db.Column(db.Boolean(), nullable=True)
    message = db.Column(db.UnicodeText(), nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)



class MarkersSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Markers

class ContentSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Content

class subContentSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "url", "txt", "content_type")







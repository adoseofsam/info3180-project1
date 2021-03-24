from . import db

class Property(db.Model):
    __tablename__ = 'tblproperties'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    rooms = db.Column(db.String(3))
    bathrooms= db.Column(db.String(3))
    price = db.Column(db.String(100))
    proptype = db.Column(db.String(80))
    location = db.Column(db.String(255))
    photo = db.Column(db.String(255))



    def __init__(self,title,description,rooms,bathrooms,price,proptype,location,photo):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.proptype = proptype
        self.location = location
        self.photo = photo

    def __repr__(self):
       return '<Property %r, $%r>' % (self.title, self.price)
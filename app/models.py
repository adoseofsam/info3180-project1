from . import db

class Property(db.Model):
    __tablename__ = 'tblproperties'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    rooms = db.Column(db.Integer)
    bathrooms= db.Column(db.Integer)
    price = db.Column(db.Integer)
    proptype = db.Column(db.String(80))
    location = db.Column(db.String(80))
    property_pic = db.Column(db.String(80))



    def __init__(self,title,description,rooms,bathrooms,price,proptype,location,property_pic):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.proptype = proptype
        self.location = location
        self.property_pic = property_pic
#
#    def is_authenticated(self):
#        return True
#
#    def is_active(self):
#        return True
#
#    def is_anonymous(self):
#        return False
#
#    def get_id(self):
#        try:
#            return unicode(self.id)  # python 2 support
#        except NameError:
#            return str(self.id)  # python 3 support
#
#    def __repr__(self):
#        return '<User %r>' % (self.id)
        
  
    

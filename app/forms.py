from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    rooms = StringField('No of Rooms', validators=[DataRequired()])
    bathrooms
    price
    proptype
    location
    photo

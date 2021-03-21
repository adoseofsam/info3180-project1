from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rooms = StringField('No. of Rooms', validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    proptype = SelectField("Property Type", [DataRequired()], choices=["House", "Apartment"])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Property Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])

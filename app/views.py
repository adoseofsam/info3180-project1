"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for,flash
from app.forms import PropertyForm
from app.models import Property
from werkzeug.utils import secure_filename



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Samantha James")


@app.route('/property', methods = ['GET', 'POST'])
def property():
    """Render the website's property page."""
    pform = PropertyForm()
    if request.method == 'POST':
        if pform.validate_on_submit():
            title = pform.title.data
            description = pform.description.data
            rooms = pform.rooms.data
            bathrooms=pform.bathrooms.data
            price = pform.price.data
            proptype = pform.price.data
            location = pform.location.data
            photo = pform.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename
            ))
            
            property=Property(title=ptitle,description=description,rooms=rooms,bathrooms=bathrooms,price=price,proptype=proptype,location=location,photo="uploads/"+filename)
            db.session.add(property)
            db.session.commit()
            
            flash('New Property has been added!','success')
            return redirect(url_for('properties'))
        else:
            flash_errors(pform)
            
    return render_template('property.html', form =pform)

@app.route('/properties', methods=['GET'])
def properties():
    """Render the website's properties page."""
    properties=[]
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/property/<propertyid>')
def getproperties(propertyid):
    """Render the website's properties page."""
    property = Property.query.get(propertyid)
    return render_template('getproperties.html', property=property)




###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")

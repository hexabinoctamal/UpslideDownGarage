"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from UpslideDownGarage import app
#from UpslideDownGarage.StoreItems import StoreItems, Apparel, Part

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('HomePage.html',
        title='Home',
        year=datetime.now().year,
        message='Message!.')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.')

@app.route('/shop')
def shop():
    return render_template('Shop.html')

@app.route('/parts')
def parts():
    return render_template('Parts.html',
        year=datetime.now().year)

@app.route('/apparel')
def apparel():
        return render_template('Apparel.html',       
        year=datetime.now().year
        )

@app.route('/accessories')
def accessories():
        return render_template('Accessories.html',       
        year=datetime.now().year,
        )

from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def getGaleria():
    obrazki = ["http://memy.pl/show/big/uploads/Post/72312/14677121051422.jpg", "https://www.wprost.pl/_thumb/d0/90/d0dd798bc6dcfd022a8eef89963a.jpeg", "https://pobierak.jeja.pl/images/4/b/a/248059_wybierz-klase-postaci.jpg"]
    return render_template('galeria.html')
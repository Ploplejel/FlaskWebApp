from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def getGalery():
    listaObrazkow = [
        'https://media.giphy.com/media/1373LnkaxqwGKQ/giphy.gif',
        'https://upload.wikimedia.org/wikipedia/commons/2/2c/Rotating_earth_%28large%29.gif',
        'http://cdn.benchmark.pl/uploads/products/5874/intel-core-i7-7700k.jpg',
        'http://arcadiawindber.com/wp-content/uploads/2017/12/ho-ho-ho-clipart.jpg',
        'https://cdn2.unrealengine.com/Fortnite%2Fbattle-royale%2Fseason6-social-1920x1080-0a72ec2f35dfe5be6cf8a77ec16063cca4db7046.jpg'
    ]
    return render_template('galeria.html', listaObrazkow=listaObrazkow, title="Galeria")
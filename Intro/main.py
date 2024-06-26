from flask import Flask
import random

app = Flask(__name__)

fakta = ['Kecanduan game online dapat menghabiskan waktu.', 
         'Kecanduan sosmed membuat hidupmu percuma.', 
         'Kecanduan shopping online dapat menghabiskan uang.']

ways = ['Mengatur berapa jam anda melihat hp atau bermain game.'
        'Menghemat uang dengan tidak berbelanja online.'
        'Pergi keluar atau mengobrol dengan teman/keluarga dari pada menghabiskan waktu dengan sosmed.']

@app.route("/")
def home():
    return '<h1>INI HALAMAN UTAMA</h1><a href="/random_facts">Klik untuk melihat fakta</a><a href="/random_ways">Klik untuk melihat cara mencegah kecanduan internet</a>'

@app.route("/random_facts")
def hello_world():
    return f"<p>Hello, World!</p><br><p>{random.choice(fakta)}</p><a href='/'>Back to Home</a>"

@app.route("/random_ways")
def randomways():
    return f"<p>Berikut ini cara mencegah kecanduan internet:</p><br><p>{random.choice(ways)}</p><a href='/'>Back to Home</a>"

app.run(debug=True)
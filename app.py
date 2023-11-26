from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Choi',
        'title': 'CSARCH2',
        'content': 'MCO2' 
    },
    {
        'author': 'Choi',
        'title': 'CSARCH2',
        'content': 'MCO2' 
    }   
]

@app.route("/")
def home():
    return render_template('home.html', posts = posts )
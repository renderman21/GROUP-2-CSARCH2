'''
    Setting Up Flask:
    1.) python -m venv venv
    2.) .\venv\Scripts\activate

    For VSC:
    3.) ctrl + shift + p pick "Choose Interpreter"
    4.) pick one with .\venv

    Terminal:
    5.) python -m pip install --upgrade pip
    6.) python -m pip install flask

    Run:
    7.) flask --app app.py --debug run
'''

# Terminal: python -m flask --app .\app.py run 
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
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
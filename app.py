from flask import Flask,render_template,url_for
from importlib import util
from importlib import reload

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('prg.html')
@app.route('/Timeline.html')
def Timeline():
    return render_template('Timeline.html')
@app.route('/BT21.html')
def BT21():
    return render_template('BT21.html')
@app.route('/Me.html')
def Me():
    return render_template('Me.html')
@app.route('/Login.html')
def Login():
    return render_template('Login.html')
    




if __name__=="__main__":
    app.run(debug=True)
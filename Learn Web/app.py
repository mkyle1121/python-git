from flask import Flask, render_template, request, session
from mysql import db

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        db.insert(name)


    return render_template('index.html')

@app.route('/submit.html',methods=['POST'])
def submit():
    text = request.form['lastname']
    return render_template('submit.html', return_text=text)

@app.route('/button', methods=['POST'])
def button1():
    if request.form['buttonpress'] == 'UP':
        print ('It went up')
    if request.form['buttonpress'] == 'DOWN':
        print ('It went down')
    return render_template('index.html')



app.run()

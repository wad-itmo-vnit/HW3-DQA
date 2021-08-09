from flask import Flask, render_template,url_for,send_file

app = Flask(__name__)

@app.route('/')
def hello_tomas():
    return render_template('index.html')

@app.route('/img/get/<num>')
def get_tomas_pics(num):
    fname = './static/pics/' + num + '.jpg'
    return send_file(fname)


app.run(host='localhost',port=5000)
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('layout.html')


@app.route('/rooms')
def rooms():
    pass


@app.route('/rates')
def rates():
    pass


@app.route('/gallery')
def gallery():
    pass


@app.route('/booking')
def booking():
    pass


@app.route('/testimonials')
def testimonials():
    pass


@app.route('/contact')
def contact():
    pass

if __name__ == '__main__':
    app.run(debug=True)

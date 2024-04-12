from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/sucess/<int:age>')
def succ(age):
    return f'your age is {age} you are eligible for voting'


@app.route('/fail/<int:age>')
def fail(age):
    return f'your age is {age} you are not eligible for voting'


@app.route('/user/<int:age>')
def user_id(age):
    if age > 18:
        return redirect(url_for('succ', age=age))
    else:
        return redirect(url_for('fail', age=age))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
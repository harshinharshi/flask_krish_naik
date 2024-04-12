from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        datascience = float(request.form['datascience'])
        c = float(request.form['c'])
        result = science + maths + datascience + c
        if result > 50:
            return render_template('result.html', result=result)
        else:
            return "failed"
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
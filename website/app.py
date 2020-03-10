from server import app
from services.init import create_services
from flask import render_template, send_file


@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html')


@app.route("/gen")
def generator():
  return render_template('generator.html')


@app.route("/sub")
def substitution():
  return render_template('substitution.html')


@app.route("/fmt")
def formatter():
  return render_template('formatter.html')


@app.route("/templater")
def templater():
  return render_template('templater.html')


@app.route("/builder")
def builder():
  return render_template('builder.html')


@app.route('/favicon.ico')
def favicon():
  return send_file('static/favicon.ico')


create_services()
if __name__ == '__main__':
    app.run(debug=True)

import flask
from flask import Flask, request, render_template,redirect
from data import add_data
import sys
import os

sys.path.insert(0, 'analysis1')
from main import linear_plot

app = Flask(__name__)


@app.route('/add/<id>')
def echo(id):
  print("Hello")
  print(request.args)
  temperature = request.args.get("Temperature")
  humidity = request.args.get("Humidity")
  gas = request.args.get('gas')
  add_data(id, temperature,humidity,gas)
  print("Temperature= ", temperature)
  return "True"


@app.route("/", methods=["GET", "POST"])
def main():
  print(request.method)
  if request.method == "POST":
    id = request.form.get("ida")
    x = request.form.get("X")
    print(id, x)
    return redirect(f"/ok/{id}?X={x}")
  else:
    return render_template("index.html")


@app.route("/ok/<ida>")
def get_data(ida):
  aa = request.args.get("X")
  try:
    os.remove("templates/{id}.html")
  except:
    pass
  linear_plot(f"{ida}", 'Timestamp', aa)
  return render_template(f"{ida}.html")


app.run(host='0.0.0.0',debug=True)

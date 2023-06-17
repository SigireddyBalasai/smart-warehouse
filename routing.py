from data import add_data,get_app
from flask import request, render_template, redirect


app = get_app()
@app.route('/add/<data_id>')
def echo(data_id):
    """Add data to the database"""
    timestamp = request.args.get("timestamp")
    temperature = request.args.get("Temperature")
    humidity = request.args.get("Humidity")
    gas = request.args.get('gas')
    add_data(data_id,timestamp, temperature, humidity, gas)
    return "Data added Successfully"


@app.route("/", methods=["GET", "POST"])
def main():
    """Main page"""
    if request.method == "POST":
        id =  request.form.get("ida")
        x =  request.form.get("X")
        return  redirect(f"/ok/{id}?X={x}")
    return  render_template("index.html")


@app.route("/ok/<ida>")
def get_data(ida):
    """Will display the data to the user using plotly"""
    return  render_template("ok.html", ida=ida)

def get_new_app():
    """Get a new app"""
    return app
from flask import Blueprint, render_template, redirect, url_for,Flask,request

app = Flask(__name__)

registration = {}
SPORTS=["Fotball", "socer","Basket"]

@app.route("/")
def home():
    return  render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name=request.form.get("name")
    if not name:
        return  render_template("fail.html")
    sport=request.form.get("sport")
    if sport not in SPORTS:
        return  render_template("fail.html")
    registration[name]=sport
    return  render_template("greet.html")

@app.route("/registrans")
def registrans():
    return  render_template("registrans.html", registrans=registration)

app.run(debug=True)

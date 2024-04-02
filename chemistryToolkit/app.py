from flask import Flask, render_template
import chemistryToolkit

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html", title = "Home")

@app.route("/about")
def about():
  return render_template("about.html", title = "About")

@app.route("/search")
def elementSearch():
  elementTable = chemistryToolkit.readTable("Periodic Table of Elements.csv")
  return render_template("elementSearch.html", title = "Element Search",
                          table = elementTable)
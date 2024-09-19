from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import ElementSearchForm

@app.route("/")
def home():
  return render_template("home.html", title = "Home")

@app.route("/about")
def about():
  return render_template("about.html", title = "About")

@app.route("/search", methods=["Get", "POST"])
def elementSearch():
  form = ElementSearchForm()
  if form.validate_on_submit():
    flash("Searching for element {}".format(form.element.data))
    return redirect(url_for('elementInfo'))
  return render_template("search.html", title = "Element Search", form=form)
#  elementTable = readTable.readTable("Periodic Table of Elements.csv")
#  return render_template("elementSearch.html", title = "Element Search",
#                          table = elementTable)

@app.route("/element", )
def elementInfo():
  return render_template("elementInfo.html")
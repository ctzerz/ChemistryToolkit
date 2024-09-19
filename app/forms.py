from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ElementSearchForm(FlaskForm):
  element = StringField("Element", validators=[DataRequired()])
  submit = SubmitField("Search")
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class getMonsters(FlaskForm):
    product = StringField('Product', validators = [DataRequired()])
    submit = SubmitField()
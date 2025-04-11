from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,FileField, SubmitField
from wtforms.validators import DataRequired, Length, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField("title", validators=[DataRequired(), Length(min=2, max=50)])
    description = TextAreaField("description", validators=[DataRequired(), Length(min=2, max=500)])
    poster = FileField("poster", validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField("Send Message")


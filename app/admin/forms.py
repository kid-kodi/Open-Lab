from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=0, max=140)])
    submit = SubmitField('Enregistrer')


class LabelForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=0, max=140)])
    submit = SubmitField('Enregistrer')


class ServiceForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=0, max=140)])
    submit = SubmitField('Enregistrer')

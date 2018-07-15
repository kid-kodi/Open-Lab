from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Length
from datetime import date


class InterviewForm(FlaskForm):
    service = SelectField(choices=[], coerce=int, label="Choisir une unité", default=(0, 'Aucun'))
    requester = StringField('Constat fait par', validators=[DataRequired()])
    request_date = StringField('Date', validators=[DataRequired()])
    request_time = StringField('Heure', validators=[DataRequired()])
    reasons = TextAreaField('Motifs de la demande', validators=[Length(min=0, max=140)])
    equipment = SelectField(choices=[], coerce=int, label="Choisir un equipement", default=(0, 'Aucun'))
    status = SelectField(choices=[(0, 'Aucun'), (1, 'Oui'), (2, 'Non')],
                         coerce=int, label="Matériel à l'arrêt ?", default=(0, 'Aucun'))
    interviewer = StringField('Intervenant', validators=[DataRequired()])
    start_date = StringField('Date de debut', validators=[DataRequired()])
    end_date = StringField('Date de fin', validators=[DataRequired()])
    actions = TextAreaField('Compte rendu de l\'intervention', validators=[Length(min=0, max=140)])
    submit = SubmitField('Enregistrer')


class OrderForm(FlaskForm):
    requester = StringField('Demandeur', validators=[DataRequired()])
    service = StringField('Lieu', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=0, max=140)])
    interviewer = StringField('Intervenant', validators=[DataRequired()])
    actions = TextAreaField('Actions effectuée', validators=[Length(min=0, max=140)])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Enregistrer')


class EquipmentForm(FlaskForm):
    category = SelectField(choices=[], coerce=int, label="Choisir une categorie")
    label = SelectField(choices=[], coerce=int, label="Choisir une marque")
    service = SelectField(choices=[], coerce=int, label="Choisir une unité")
    name = StringField('Nom')
    model = StringField('Modèle')
    serial = StringField('Numéro de serie')
    arrived_at = DateField('Date d\'arrivée', format="%m/%d/%Y")
    description = TextAreaField('Description')
    submit = SubmitField('Enregistrer')

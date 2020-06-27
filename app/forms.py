from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class FeedbackForm(FlaskForm):
    fbSubject = StringField('Feedback for: ',render_kw={'readonly': True})
    yourname = StringField('Your Name', validators=[DataRequired()])
    contact = StringField('email', validators=[DataRequired(), Email()])
    copyright = BooleanField('Is this a copyright/ownership query?')
    privacy = BooleanField('Is this a safety/privacy query?')
    message = TextAreaField('Message', validators=[Length(min=1, max=360)])
    submit = SubmitField('Send')
    cancel = SubmitField('cancel')
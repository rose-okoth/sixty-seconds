from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch Title',validators=[Required()])
    text = TextAreaField('Pitch Description',validators=[Required()])
    category = SelectField('Type',choices=[('interview','Interview Pitch'),('advertisement','Advertisement Pitch'),('promotion','Promotion Pitch'),('quote','Quote Pitch'),('school','School Pitch'),('project','Project Pitch')],validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')

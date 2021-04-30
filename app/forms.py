from flask_wtf          import FlaskForm 
from wtforms            import StringField, PasswordField, BooleanField, SubmitField 
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo 
from app.models         import User

class LoginForm(FlaskForm):

    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('all done')

class RegistrationForm(FlaskForm):

    username = StringField('username', validators = [DataRequired()])
    email = StringField('email', validators = [DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired()])
    password_again = PasswordField(
        'password again', 
        validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('all done')

    def validate_username(self, username):

        user = User.query.filter_by(username = username.data).first()

        if user is not None:
            raise ValidationError("username is taken. roll again.")

    def validate_email(self, email):

        user = User.query.filter_by(email = email.data).first()

        if user is not None:
            raise ValidationError("this email is already in our system")

    
from flask_wtf          import FlaskForm 
from wtforms            import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models         import User
from flask_babel        import _, lazy_gettext as _l

class LoginForm(FlaskForm):

    username = StringField(_l('username'), validators = [DataRequired()])
    password = PasswordField(_l('password'), validators = [DataRequired()])
    remember_me = BooleanField(_l('remember me'))
    submit = SubmitField(_l('all done'))

class RegistrationForm(FlaskForm):

    username = StringField(_l('username'), validators = [DataRequired()])
    email = StringField(_l('email'), validators = [DataRequired(), Email()])
    password = PasswordField(_l('password'), validators = [DataRequired()])
    password_again = PasswordField(
        _l('password again'), 
        validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('all done'))

    def validate_username(self, username):

        user = User.query.filter_by(username = username.data).first()

        if user is not None:
            raise ValidationError(_("username is taken. roll again."))

    def validate_email(self, email):

        user = User.query.filter_by(email = email.data).first()

        if user is not None:
            raise ValidationError(_("this email is already in our system"))

class ResetPasswordRequestForm(FlaskForm):

    email = StringField(_l('email'), validators = [DataRequired(), Email()])
    
    submit = SubmitField(_l('reset password please'))

class ResetPasswordForm(FlaskForm):

    password = PasswordField(_l('password'), validators = [DataRequired()])
    
    password_again = PasswordField(
        _l('password_again'), validators = [DataRequired(), EqualTo('password')]
    )

    submit = SubmitField(_l('reset my password please'))

    
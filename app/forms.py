from flask_wtf          import FlaskForm 
from wtforms            import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo , Length
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

class EditProfileForm(FlaskForm):

    username = StringField('username',   validators = [DataRequired()])
    about_me = TextAreaField('about me', validators = [Length(min = 0, max = 128)])

    submit = SubmitField('all done')

    def __init__(self, original_username, *args, **kwargs):

        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.original_username = original_username

    def validate_username(self, username):

        if username.data != self.original_username:

            user = User.query.filter_by(username = self.username.data).first()

            if user is not None:
                raise ValidationError('username taken. roll again.')

class EmptyForm(FlaskForm):

    submit = SubmitField('submit')

class PostForm(FlaskForm):

    post = TextAreaField("what's on your mind", validators = [
        DataRequired(), Length(min = 1, max = 256)
    ])

    submit = SubmitField('post it')

class ResetPasswordRequestForm(FlaskForm):

    email = StringField('email', validators = [DataRequired(), Email()])
    
    submit = SubmitField('reset password please')

class ResetPasswordForm(FlaskForm):

    password = PasswordField('password', validators = [DataRequired()])
    
    password_again = PasswordField(
        'password_again', validators = [DataRequired(), EqualTo('password')]
    )

    submit = SubmitField('reset my password please')

    
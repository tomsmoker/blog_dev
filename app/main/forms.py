from flask              import request
from flask_wtf          import FlaskForm 
from wtforms            import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models         import User
from flask_babel        import _, lazy_gettext as _l

class EditProfileForm(FlaskForm):

    username = StringField(_l('username'),   validators = [DataRequired()])
    about_me = TextAreaField(_l('about me'), validators = [Length(min = 0, max = 128)])

    submit = SubmitField(_l('all done'))

    def __init__(self, original_username, *args, **kwargs):

        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.original_username = original_username

    def validate_username(self, username):

        if username.data != self.original_username:

            user = User.query.filter_by(username = self.username.data).first()

            if user is not None:
                raise ValidationError(_('username taken. roll again.'))

class EmptyForm(FlaskForm):

    submit = SubmitField(_l('submit'))

class PostForm(FlaskForm):

    post = TextAreaField(_l("what's on your mind"), validators = [
        DataRequired(), Length(min = 1, max = 256)
    ])

    submit = SubmitField(_l('post it'))

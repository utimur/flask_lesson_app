from wtforms import Form, StringField, TextAreaField

class PostForm(Form):
    tittle = StringField('Tittle')
    body = TextAreaField('Body')
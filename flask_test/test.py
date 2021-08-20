from flask import Flask, jsonify, request
from flask.scaffold import F

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)

@app.route('/locales')
def locales():
    return jsonify(['ru', 'en', 'it'])


@app.route('/sum/<int:first>/<int:second>')
def sum(first, second):
    return str(first + second)


@app.route('/great/<username>')
def Hello(username):
    return f'Hello, {username}'

errors = []
class ContactForm(FlaskForm):
 
    email = StringField(validators=[
            validators.Length(min = 6, max = 35), 
            validators.Email()
    ])
    password = PasswordField(validators=[
            validators.Length(min=4, max=30),
            validators.DataRequired(),
            validators.equal_to('confirm', message='Passwords must match')
    ])
    confirm = PasswordField() 




@app.route('/form/user', methods=['GET', 'POST'])
def accept_user_data():
    if request.method == 'POST':
        form = ContactForm(request.form)

        if form.validate():
            return jsonify({
                'status': 1,
                'email': form.email.data,
                'password': form.password.data,
            })
        else:
            return jsonify({
                'status': 0,
            })
    
    if request.method == 'GET':
        return ('You must use POST method!!!', 200)


if __name__ == '__main__':
    app.run()


import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

load_dotenv('.env')


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Log in')


app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.getenv('SECRETKEY')
admin_email = os.getenv("EMAIL")
admin_password = os.getenv("PASSWORD")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == admin_email and login_form.password.data == admin_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

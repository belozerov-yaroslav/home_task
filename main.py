from flask import Flask, url_for, request, render_template, redirect
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import os
import json
from datetime import datetime
from random import randint
from ORM.data.users import User

from ORM.data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = '2109210139122q1q12djmkiosejowaseiju'


class RegisterForm(FlaskForm):
    email = EmailField('Login/email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age')
    spec = StringField('Speciality')
    address = StringField('Address')
    submit = SubmitField('Submit')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Parols must be equal")
        db_session.global_init('ORM/db/mars_explorer.db')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="This email is currently using")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            age=form.age.data,
            speciality=form.spec.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/register')
    return render_template('register.html', form=form, title='Регистрация', message='')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

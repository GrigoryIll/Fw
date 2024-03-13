from flask import Flask, render_template, request
from models import db, User
from forms import RegisterForm
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
db.init_app(app)

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        user = User(name = name, surname = surname, email = email, password = password )
        db.session.add(user)
        db.session.commit()
        return "Вы зарегистрированы"
    return render_template('register.html', form=form)
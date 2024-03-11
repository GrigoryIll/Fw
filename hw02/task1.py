from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e'

@app.route('/')
def base():
    return render_template('base.html')


@app.route('/', methods=['GET', 'POST'])
def fill():
    if request.method == 'POST':
        session["name"] = request.form.get('name')
        session["email"] = request.form.get('email')
        return redirect(url_for('auth', name=session["name"]))
    
    
@app.route('/auth/<name>', methods=['GET', 'POST'])
def auth(name):
    return render_template('auth.html', name=name)
    

@app.route('/logout')
def logout():
    session.pop('name', None)
    session.pop('email', None)
    return redirect(url_for('base'))

if __name__ == '__main__':
    app.run()
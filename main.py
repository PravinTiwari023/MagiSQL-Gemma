from flask import Flask, request, session, render_template, redirect, url_for
import firebase_setup

# Initialize Firebase
auth = firebase_setup.auth
db = firebase_setup.db

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Yaha pe ek strong secret key dal dena

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def perform_login():
    email = request.form['email']
    password = request.form['password']

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        # Store the user's id token in the session
        user_id = user['localId']
        session['user_id'] = user_id
        return render_template('home.html')
    except:
        return render_template('login.html', message='Email does not exists')

@app.route('/register', methods=['POST'])
def perform_register():
    email = request.form['email']
    password = request.form['password']

    try:
        user = auth.create_user_with_email_and_password(email, password)
        return render_template('login.html', message='Register successful.')
    except:
        return render_template('register.html', message='Email already exists')

@app.route('/submit', methods=['POST'])
def save_data():
    name = request.form['name']
    level = request.form['level']
    data = {"name": name, "level": level}
    db.child("users").push(data)
    return 'Data submitted successfully!'

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

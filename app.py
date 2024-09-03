from flask import Flask, request, render_template, redirect, url_for
import re

app = Flask(__name__)

# Helper function to validate password
def validate_password(password):
    if len(password) < 5 or len(password) > 16:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not re.search(r'[@_!#$%^&*()<>?/\|}{~:]', password):
        return False
    return True

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate username
        if not (re.search(r'@gmail\.com$', username) and re.search(r'^[a-zA-Z]', username)):
            return "Invalid Username/Email. Please enter a correct format, e.g., abcd@gmail.com"

        # Validate password
        if not validate_password(password):
            return "Invalid Password. Ensure it meets the required criteria."

        with open('projectdatabase.txt', 'a+') as file:
            file.write(f"{username}, {password}\n")

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open('projectdatabase.txt', 'r') as file:
            users = [line.strip().split(', ') for line in file]

        user_dict = {user[0]: user[1] for user in users}

        if username in user_dict and user_dict[username] == password:
            return redirect(url_for('welcome'))
        else:
            return "Invalid Username or Password. Please try again."

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

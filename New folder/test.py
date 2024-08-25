from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required to use sessions

# Sample user data
users = {"chaitanya@ac.in": 'comp'}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check login credentials
        if email in users and users[email] == password:
            session['logged_in'] = True
            session['email'] = email
            return redirect(url_for('index'))  # Redirect to main page after login
        else:
            # Invalid credentials, stay on login page with error message
            return render_template('login.html', error="Invalid email or password.")
    
    # Show login page if GET request or not logged in
    return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    # Redirect to login if not logged in
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('home'))

    if request.method == 'POST':
        comment = request.form.get('comment')
        print(f"Comment: {comment}")
        # Here, you could save the comment to a database or perform other actions

        # Return a JSON response
        return jsonify({"comment": comment})

    return render_template('index.htm', email=session.get('email'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('email', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

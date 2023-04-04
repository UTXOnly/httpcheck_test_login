from flask import Flask, render_template, request, redirect, make_response
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

# Mock user database
users = {os.environ.get('DB_USERNAME'): os.environ.get('DB_PASSWORD')}
app.logger.debug(f"Users: {users}")

app.logger.debug(os.environ)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    app.logger.debug("Rendering login template")
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    db_username = os.environ.get('DB_USERNAME')
    db_password = os.environ.get('DB_PASSWORD')

    if username == db_username and password == db_password:
        # Set a cookie to mark the user as authenticated
        app.logger.debug(f"User {username} authenticated")
        resp = make_response(redirect('/protected'))
        resp.set_cookie('authenticated', 'true')
        return resp
    else:
        app.logger.debug(f"Invalid login attempt for user {username}")
        return render_template('invalid_login.html')


@app.route('/logout')
def logout():
    # Clear the authentication cookie or session variable
    resp = make_response(render_template('login.html'))
    resp.delete_cookie('authenticated')
    return resp

@app.route('/protected')
def protected():
    # Check for the presence of the authentication cookie or session variable
    authenticated = request.cookies.get('authenticated')
    if authenticated != 'true':
        app.logger.debug("Unauthenticated user attempting to access protected page")
        return redirect('/login')
    else:
        app.logger.debug("Rendering protected template")
        return render_template('protected.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Mock user database
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Set a cookie to mark the user as authenticated
        resp = make_response(redirect('/protected'))
        resp.set_cookie('authenticated', 'true')
        return resp
    else:
        return "Invalid login credentials"

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
        return redirect('/login')
    else:
        return render_template('protected.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



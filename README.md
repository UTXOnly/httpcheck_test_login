

# httpcheck_test_login README

This is a simple login form web application built using HTML, CSS, and Flask. The application provides a secure login and authentication system for users, allowing them to sign in with their username and password.

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/UTXOnly/httpcheck_test_login.git`
2. Navigate to the project directory using `cd httpcheck_test_login`
3. Install the required dependencies listed in the `requirements.txt` file by running `pip install -r requirements.txt` from a `BASH` terminal
4. To start the containerized application, navigate to the `httpcheck_test_login` directory in a `BASH` terminal and run the following command: `docker-compose up --build`

### Example .env file

```
SECRET_KEY=test_key
DB_USERNAME=user
DB_PASSWORD=password
```

## Usage

1. Open your web browser and go to `http://localhost:5000` 
2. Enter your username and password credentials and click the Submit button
3. If the credentials are correct, you will be redirected to a success page. Otherwise, an error message will be displayed on the login page.

## Contributing

If you find any issues with the application or if you would like to suggest new features, please open an issue or submit a pull request with your changes.

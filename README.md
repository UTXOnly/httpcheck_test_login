Here's the updated README to reflect the containerized application and Docker Compose environment variable:

# Web Application README

This is a simple login form web application built using HTML, CSS, and Flask. The application provides a secure login and authentication system for users, allowing them to sign in with their username and password.

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/UTXOnly/httpcheck_test_login.git`
2. Navigate to the project directory using `cd httpcheck_test_login`
3. Install the required dependencies listed in the `requirements.txt` file by running `pip install -r requirements.txt` from a `BASH` terminal
4. To start the containerized application, navigate to the `httpcheck_test_login` directory in a `BASH` terminal and run the following command: `docker-compose up --build`. Note that you can customize the port number that the application runs on by setting the `WEB_APP_PORT` environment variable in the `.env` file.

## Usage

1. Open your web browser and go to `http://localhost:{port_number}` to view the login page (where `{port_number}` is replaced with the port number specified in the `.env` file or default of 8000 if not set)
2. Enter your username and password credentials and click the Submit button
3. If the credentials are correct, you will be redirected to a success page. Otherwise, an error message will be displayed on the login page.

## Contributing

If you find any issues with the application or if you would like to suggest new features, please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/<your-username>/<repo-name>/blob/master/LICENSE) file for more details.
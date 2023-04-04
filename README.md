

# httpcheck_test_login README

This is a simple login form web application built using HTML, CSS, and Flask. The application provides a secure login and authentication system for users, allowing them to sign in with their username and password.

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/UTXOnly/httpcheck_test_login.git`
2. Navigate to the project directory using `cd httpcheck_test_login`
3. Install the required dependencies listed in the `requirements.txt` file by running `pip install -r requirements.txt` from a `BASH` terminal
4. To start the containerized application, navigate to the `httpcheck_test_login` directory in a `BASH` terminal and run the following command: `docker-compose up --build`



### Example .env file

The `.env` file is used to store environment variables that are specific to your local machine or deployment environment. In this project, we use it to set the `SECRET_KEY`, `DB_USERNAME`, and `DB_PASSWORD` values that are used by Flask.

To fill out the `.env` file, follow these steps:

1. Open a text editor such as Notepad, Sublime Text, or Visual Studio Code.
2. Create a new file in the root directory of the project.
3. Save the file with the name ".env" (without the quotes) - Note that the filename starts with a dot, which means it's a hidden file on Unix-based systems like Linux and macOS.
4. Add the following lines with their corresponding values:

```
SECRET_KEY=test_key
DB_USERNAME=user
DB_PASSWORD=password
```

Note that these values are just examples and should be replaced with your own values. The `SECRET_KEY` is used by Flask to encrypt session data, while `DB_USERNAME` and `DB_PASSWORD` are used to authenticate and authorize access to a database.

Once you have filled out the `.env` file, save it and make sure it is located in the root directory of the project. Flask will automatically read this file when it starts up and load the values as environment variables.


## Usage

1. Open your web browser and go to `http://localhost:3007` 
2. Enter your username and password credentials and click the Submit button
3. If the credentials are correct, you will be redirected to a success page. Otherwise, an error message will be displayed on the login page.

## Contributing

If you find any issues with the application or if you would like to suggest new features, please open an issue or submit a pull request with your changes.

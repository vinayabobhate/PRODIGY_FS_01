# PRODIGY_FS_01
This is a simple Flask-based authentication system that allows users to register with a valid email address and a secure password, log in, and access a welcome page. The application also includes basic password validation to ensure the security of user accounts.

## Features

- **User Registration**: Users can register with a Gmail address and a secure password.
- **User Login**: Registered users can log in with their credentials.
- **Password Validation**: The password must meet specific criteria, including length, character types, and special symbols.
- **Welcome Page**: After successful login, users are redirected to a welcome page.
- **Logout**: Users can log out and be redirected to the login page.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/flask-auth-system.git
    cd flask-auth-system
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Open your browser and navigate to `http://127.0.0.1:5000/`.

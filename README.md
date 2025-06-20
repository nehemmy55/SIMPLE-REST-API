# Simple User Management API

This is a simple REST API built with Python using the Flask framework. It allows you to:

    . Create users
    . Retrieve a specific user by ID
    . List all users

User data is stored in a local JSON file (users.json).

# Tech Stack

    . Language: Python 3.x
    . Framework: Flask
    . Storage: JSON file for persistence
    . Postman: for easy way for postign users or getting users

# Setup Instructions

1. Save API.py

Save your Flask code into a file named API.py in your project directory.

2. Create and Activate a Virtual Environment (Optional but Recommended)

python3 -m venv venv
# On Windows
.\venv\Scripts\activate


3. Install Dependencies

pip install Flask


4. Create an Empty users.json File

echo "{}" > users.json


5. Run the Application

python app.py


By default, it runs on http://localhost:5000.

# Example Requests

# Create a New User

POST /users

curl -X POST http://localhost:5000/users \ -H "Content-Type: application/json" \ -d '{"name": "Alice", "email": "alice@example.com"}' 

# Get a Specific User

GET /users/<user_id>

curl http://localhost:5000/users/<user_id>


Replace <user_id> with the actual UUID returned from the POST request.

# Get All Users

GET /users

curl http://localhost:5000/users


# Project Structure

├── app.py              # Flask API

├── users.json          # User data storage

└── README.md           # This documentation

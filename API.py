from flask import Flask, request, jsonify
import uuid
import json
"""make flask application """
app = Flask(__name__)

""" This empty dictionary will hold our user information"""
users = {}

@app.route('/users', methods=['POST'])
def create_user():
    """This function creates a new user"""
    data = request.get_json()

    """Make sure the user sent us a name and an email"""
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "You need to send a name and email"}), 400

    """ Create a unique auto increment ID for the new user."""
    user_id = str(uuid.uuid4())
    new_user = {
        'id': user_id,
        'name': data['name'],
        'email': data['email']
    }
    # """Save the new user's information"""
    with open('users.json', 'r') as users_file:
        users = json.load(users_file if users_file else dict())
        users[user_id] = new_user
    with open('users.json', 'w') as users_file:
        users_file.write(json.dumps(users, indent=4))

    return jsonify(new_user), 201


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """This function finds a user by their ID."""
    with open('users.json', 'r') as users_file:
        users = json.load(users_file if users_file else dict())
        if user_id not in users:
            return jsonify({"error": "User not found"}), 404

    """ If we find the user, send back their information."""
    return jsonify(users[user_id]), 200

#endpoint for displaying all users
@app.route('/users', methods=['GET'])
def get_users():
    """This function returns all users."""
    with open('users.json', 'r') as users_file:
        users = json.load(users_file if users_file else dict())
    return jsonify(users), 200

if __name__ == '__main__':
    print("http://localhost:5000/users")
    app.run(debug=True, port=5000)

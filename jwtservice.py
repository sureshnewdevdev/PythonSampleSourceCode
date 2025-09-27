from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import os

app = Flask(__name__)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your-secret-key-change-in-production')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=9000)
app.config['JWT_ALGORITHM'] = 'HS256'

jwt = JWTManager(app)

# Sample user database (use a real database in production)
USERS = {
    'admin': {'password': 'password123', 'role': 'admin', 'email': 'admin@example.com'},
    'user': {'password': 'userpass', 'role': 'user', 'email': 'user@example.com'},
    'demo': {'password': 'demo123', 'role': 'demo', 'email': 'demo@example.com'}
}

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to obtain JWT token"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = USERS.get(username)
    if user and user['password'] == password:
        additional_claims = {'role': user['role'], 'email': user['email']}
        access_token = create_access_token(identity=username, additional_claims=additional_claims)
        return jsonify({
            'success': True,
            'access_token': access_token,
            'token_type': 'Bearer',
            'expires_in': 900,
            'user': {'username': username, 'role': user['role'], 'email': user['email']}
        })
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    user_data = USERS.get(current_user, {})
    return jsonify({
        'success': True,
        'message': f'Hello {current_user}! This is a protected endpoint.',
        'user': current_user,
        'role': user_data.get('role'),
        'data': ['item1', 'item2', 'item3']
    })

@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    user_data = USERS.get(current_user)
    if not user_data:
        return jsonify({'success': False, 'message': 'User not found'}), 404
    return jsonify({
        'success': True,
        'username': current_user,
        'role': user_data['role'],
        'email': user_data['email'],
        'profile_data': {
            'last_login': '2024-01-15 10:30:00',
            'preferences': {'theme': 'dark', 'language': 'en'}
        }
    })

@app.route('/public', methods=['GET'])
def public():
    return jsonify({
        'success': True,
        'message': 'This is a public endpoint, no authentication required!'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
    
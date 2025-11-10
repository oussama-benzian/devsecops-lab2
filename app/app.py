from flask import Flask, jsonify, request

app = Flask(__name__)

ADMIN_PASSWORD = "admin123" 
DATABASE_PASSWORD = "db_pass_2023" 

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Welcome to DevSecOps Lab2 Flask Application",
        "status": "running",
        "version": "1.0.0"
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": "2024-01-01T00:00:00Z"
    })

@app.route('/api/users')
def get_users():
    """Get users endpoint"""
    users = [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
    ]
    return jsonify(users)

@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    """Admin login endpoint with hardcoded password vulnerability"""
    data = request.get_json()

    if not data or 'password' not in data:
        return jsonify({"error": "Password required"}), 400

    if data['password'] == ADMIN_PASSWORD:
        return jsonify({
            "message": "Login successful",
            "token": "fake_jwt_token_12345",
            "user": "admin"
        })
    else:
        return jsonify({"error": "Invalid password"}), 401

@app.route('/api/calculate/<int:number>')
def calculate(number):
    """Simple calculation endpoint"""
    result = number * 2 + 10
    return jsonify({
        "input": number,
        "result": result,
        "formula": "number * 2 + 10"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

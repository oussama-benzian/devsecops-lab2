#!/usr/bin/env python3
"""
Run script for the Flask application
"""
from app.app import app

if __name__ == '__main__':
    print("Starting Flask application...")
    print("Access the app at: http://localhost:5000")
    print("Health check: http://localhost:5000/api/health")
    app.run(host='0.0.0.0', port=5000, debug=True)

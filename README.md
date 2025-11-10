# DevSecOps Lab 2: Python Application with CI/CD Pipeline

This project demonstrates the implementation of DevSecOps practices for a Python Flask application using Docker, Jenkins CI/CD, and security scanning tools.

## Overview

The project implements a complete DevSecOps pipeline that integrates security testing throughout the development and deployment lifecycle. The application is a simple REST API built with Flask, containerized using Docker, and deployed through an automated Jenkins pipeline.

## Features

- RESTful API with endpoints for health checks, user management, and calculations
- Comprehensive test suite using pytest
- Docker containerization with multi-stage builds
- Automated CI/CD pipeline with Jenkins
- Security scanning integration (Bandit, Trivy, Safety)
- GitHub-based version control

## API Endpoints

- `GET /` - Application information
- `GET /api/health` - Health check
- `GET /api/users` - User data
- `POST /api/admin/login` - Admin authentication
- `GET /api/calculate/<number>` - Mathematical calculations

## Technology Stack

- **Backend**: Python Flask
- **Testing**: pytest with pytest-flask
- **Containerization**: Docker & Docker Compose
- **CI/CD**: Jenkins Pipeline
- **Security Tools**:
  - Bandit (static code analysis)
  - Trivy (container vulnerability scanning)
  - Safety (dependency vulnerability checking)
- **Version Control**: Git with GitHub

## Local Development

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/oussama-benzian/devsecops-lab2.git
cd devsecops-lab2

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest app/tests/ -v

# Run application locally
python run.py
```

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build

# Access application at http://localhost:5000
```

## CI/CD Pipeline

The Jenkins pipeline automates the following stages:

1. **Checkout** - Pull latest code from GitHub
2. **Install Dependencies** - Set up Python virtual environment
3. **Run Tests** - Execute pytest test suite
4. **Security Analysis** - Bandit static code analysis
5. **Container Scanning** - Trivy vulnerability assessment
6. **Dependency Check** - Safety package vulnerability scanning
7. **Build** - Create Docker image
8. **Deploy** - Run application with health verification

## Security Features

The pipeline integrates multiple security scanning tools:

- **Bandit** detects hardcoded passwords, debug mode usage, and other security issues
- **Trivy** scans Docker images for known vulnerabilities
- **Safety** checks Python dependencies against vulnerability databases

## Project Structure

```
devsecops-lab2/
├── app/
│   ├── __init__.py
│   ├── app.py              # Flask application
│   └── tests/
│       └── test_app.py     # Test suite
├── Dockerfile              # Container definition
├── docker-compose.yml      # Service orchestration
├── Jenkinsfile             # CI/CD pipeline
├── requirements.txt        # Python dependencies
├── pytest.ini             # Test configuration
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Usage

The application provides a REST API for basic operations. After deployment, the API is available at the configured endpoints with comprehensive health monitoring and security scanning integrated into the deployment pipeline.

## Contributing

This is an educational project demonstrating DevSecOps principles. For modifications, ensure all security scans pass and tests are maintained.
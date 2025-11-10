pipeline {
    agent any
    environment {
        // Set up Python and Docker
        PYTHON_IMAGE = 'python:3.9-slim'
        IMAGE_NAME = 'devsecops-lab2-web'
    }
    stages {
        stage('Checkout') {
            steps {
                // Pull the code from GitHub
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install Python dependencies
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the tests with pytest
                    sh 'cd /var/lib/jenkins/workspace/DevSecOps-Lab2-Pipeline && PYTHONPATH=/var/lib/jenkins/workspace/DevSecOps-Lab2-Pipeline ./venv/bin/pytest app/tests/'
                }
            }
        }

        stage('Static Code Analysis (Bandit)') {
            steps {
                script {
                    // Run Bandit for static code analysis
                    sh './venv/bin/bandit -r app/'
                }
            }
        }

        stage('Container Vulnerability Scan (Trivy)') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker-compose build'
                    // Scan the image with Trivy
                    sh 'trivy image ${IMAGE_NAME}:latest'
                }
            }
        }

        stage('Check Dependency Vulnerabilities (Safety)') {
            steps {
                script {
                    // Run Safety to check dependencies
                    sh './venv/bin/safety check -r requirements.txt'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker-compose build'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    // Deploy the application using Docker Compose
                    sh 'docker-compose up -d'
                    sh 'sleep 5'
                    sh 'curl -f http://localhost:5000/api/health'
                }
            }
        }
    }
    post {
        always {
            // Clean up after build
            cleanWs()
        }
    }
}

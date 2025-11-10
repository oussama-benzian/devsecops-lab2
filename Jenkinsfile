pipeline {
    agent any
    environment {
        PYTHON_IMAGE = 'python:3.9-slim'
        IMAGE_NAME = 'devsecops-lab2-web'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh './venv/bin/pytest app/tests/ -v'
                }
            }
        }

        stage('Static Code Analysis (Bandit)') {
            steps {
                script {
                    sh 'bandit -r app/'
                }
            }
        }

        stage('Container Vulnerability Scan (Trivy)') {
            steps {
                script {
                    sh 'docker-compose build'
                    sh 'trivy image ${IMAGE_NAME}:latest'
                }
            }
        }

        stage('Check Dependency Vulnerabilities (Safety)') {
            steps {
                script {
                    sh 'safety check -r requirements.txt'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh 'docker-compose up -d'
                    sh 'sleep 5'
                    sh 'curl -f http://localhost:5000/api/health'
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}

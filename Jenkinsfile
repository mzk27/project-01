pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                script {
                    echo '--- Checking out SCM ---'
                    checkout scm
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo '--- Installing Dependencies ---'
                    // Create virtual environment
                    sh 'python3 -m venv venv'
                    // Activate Virtual Environment
                    sh 'chmod +x venv/bin/activate'
                    sh '. venv/bin/activate'
                    // Install required packages and modules
                    sh 'venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Testing') {
            steps {
                script {
                    echo '--- Running Tests ---'
                    sh 'venv/bin/pytest -s test_calculator.py'
                }
            }
        }
    }
}

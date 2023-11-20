pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
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
                    sh 'venv/bin/pytest -s test_calculator.py'
                }
            }
        }

        stage('Pull Deployment Scripts') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/mzk27/deploy-config.git'
                }
            }
        }

        stage('Deployment') {
            steps {
                script {
                    ansiblePlaybook (
                        credentialsId: 'jenkins-private-key',
                        installation: 'Ansible',
                        inventory: '/etc/ansible/hosts',
                        playbook: '/var/lib/jenkins/workspace/Flask_App/deployment/roles/playbook.yml',
                        vaultTmpPath: ''
                        // Add any other parameters as needed
                    )
                }
            }
        }
    }
}

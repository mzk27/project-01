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

        stage('Pull Deployment Scripts') {
            steps {
                script {
                    echo '--- Pulling Deployment Scripts ---'
                    git branch: 'main', url: 'https://github.com/mzk27/deploy-config.git'
                }
            }
        }

        stage('Deployment') {
            steps {
                script {
                    echo '--- Before Ansible Playbook ---'
                    sh 'ls -lrt /var/lib/jenkins/workspace/Flask_App/deployment/roles/tasks'

                    echo '--- Running Ansible Playbook ---'
                    ansiblePlaybook (
                        credentialsId: 'jenkins-private-key',
                        installation: 'Ansible',
                        inventory: '/etc/ansible/hosts',
                        playbook: '/var/lib/jenkins/workspace/Flask_App/deployment/roles/playbook.yml',
                        vaultTmpPath: ''
                        // Add any other parameters as needed
                    )

                    echo 'After Ansible Playbook'
                    sh 'ls -lrt /var/lib/jenkins/workspace/Flask_App/deployment/roles/tasks'
                }
            }
        }
    }

    post {
        failure {
            echo '--- Pipeline Failed ---'
        }
    }
}

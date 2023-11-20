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
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install -r requirements.txt'
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
                    git branch: 'main', credentialsId: 'your-credentials-id', url: 'https://github.com/mzk27/deploy-config.git'
                }
            }
        }

        stage('Deployment') {
            steps {
                script {
                    echo '--- Before Ansible Playbook ---'
                    sh 'ls -lrt /var/lib/jenkins/workspace/Flask_App/deployment/roles/tasks'

                    echo '--- Running Ansible Playbook ---'
                    sh '/usr/bin/ansible-playbook /var/lib/jenkins/workspace/Flask_App/deployment/roles/playbook.yml -i /etc/ansible/hosts'
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

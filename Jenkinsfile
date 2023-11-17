pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                script {
                    sh 'python -m venv venv'
                }
            }
        }

        stage('Activate Virtual Environment') {
            steps {
                script {
                    sh 'source venv/bin/activate'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Build and Run Flask App') {
            steps {
                script {
                    sh 'venv/bin/python app.py'
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

        stage('Deactivate Virtual Environment') {
            steps {
                script {
                    sh 'deactivate'
                }
            }
        }

        stage('Deploy') {
            //steps {
            //    script {
            //        ansiblePlaybook inventory: '~/ansible/hosts', playbook: '~/ansible/deploy_playbook.yml', vaultTmpPath: ''
                }
            }
        }
    }
}
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

        // stage('Deploy') {
        //     steps {
        //         script {
        //             // Replace placeholder paths with actual paths
        //             ansiblePlaybook inventory: '~/ansible/hosts', playbook: '~/ansible/deploy_playbook.yml', vaultTmpPath: ''
        //         }
        //     }
        // }
    }
}
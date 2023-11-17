pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Print Environment') {
            steps {
                script {
                    sh 'echo "PATH: $PATH"'
                    sh 'echo "PYTHONPATH: $PYTHONPATH"'
                    sh 'echo "which python3: $(which python3)"'
                }
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                script {            
                    // Create virtual environment
                     sh 'python3 -m venv venv'
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
                    sh 'venv/bin/python3 app.py'
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
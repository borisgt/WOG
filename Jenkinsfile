pipeline {
    agent any

    environment {
        FLASK_PORT = '8777'
        DOCKER_USERNAME = credentials('docker-username')
        DOCKER_PASSWORD = credentials('docker-password')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'docker-compose up -d flask_wog'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    def testResult = sh(script: "python3 e2e.py", returnStatus: true)
                    if (testResult != 0) {
                        error("Tests failed")
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker-compose down'
                    sh 'docker-compose run push_to_dockerhub'
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
pipeline {
    agent any

    environment {
        FLASK_PORT = '8777'
        DOCKER_USERNAME = credentials('docker-username')
        DOCKER_PASSWORD = credentials('docker-password')
        GITHUB_TOKEN = credentials('github-token')
        PATH = "/usr/local/bin:$PATH"
        IMAGE_NAME = 'flask_wog'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'echo $PATH'
                    sh 'docker compose build'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'docker compose up -d flask_wog'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    def testResult = sh(script: "docker compose run test", returnStatus: true)
                    if (testResult != 0) {
                        error("Tests failed")
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh """
                    docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}
                    docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                    docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker compose down'
                    sh """
                    docker image rm ${IMAGE_NAME}:${IMAGE_TAG} -f
                    docker image rm ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} -f
                    """
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
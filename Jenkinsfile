pipeline {
    agent any

    environment {
        FLASK_PORT = '8777'
        DOCKER_USERNAME = credentials('docker-username')
        DOCKER_PASSWORD = credentials('docker-password')
        PATH = "/usr/local/bin:$PATH"
        IMAGE_NAME = 'flask_wog'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Build') {
            steps {
                script {
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
                    if (testResult == 0) {
                        echo "Tests succeeded!"
                    } else {
                        error("Tests failed.")
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        echo "DOCKER_USERNAME is: ${DOCKER_USERNAME}"
                        echo "DOCKER_PASSWORD is: ${DOCKER_PASSWORD}"

                        sh """
                        echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin
                        docker tag ${IMAGE_NAME}:${IMAGE_TAG} \$DOCKER_USERNAME/${IMAGE_NAME}:${IMAGE_TAG}
                        docker push \$DOCKER_USERNAME/${IMAGE_NAME}:${IMAGE_TAG}
                        """
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker compose down'
                }
            }
        }
    }

    post {
        always {
            script {
                sh 'docker system prune -f'
                sh 'docker rmi ${IMAGE_NAME}:${IMAGE_TAG}'
                cleanWs()
            }
        }
    }
}
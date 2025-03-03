pipeline {
    agent any

    environment {
        REGISTRY = "borisgt/wog"
        REGISTRY_CREDENTIAL = 'dockerhub_id'
        FLASK_PORT = '8777'
        DOCKER_IMAGE = ''
        PATH = "/usr/local/bin:$PATH"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    DOCKER_IMAGE = REGISTRY + ":$BUILD_NUMBER"
                    sh 'docker compose build'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'docker compose up -d ${DOCKER_IMAGE}'
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

        /*
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        sh """
                        echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin
                        docker tag ${IMAGE_NAME}:${IMAGE_TAG} \$DOCKER_USERNAME/${IMAGE_NAME}:${IMAGE_TAG}
                        docker push \$DOCKER_USERNAME/${IMAGE_NAME}:${IMAGE_TAG}
                        """
                    }
                }
            }
        }
        */

        stage('Deploy image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry( '', REGISTRY_CREDENTIAL ) {
                        DOCKER_IMAGE.push()
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
                sh """
                if [ \$(docker ps -aq -f name=wog_flask_container) ]; then
                    docker rm -f wog_flask_container
                fi
                if [ \$(docker ps -aq -f name=wog_test_container) ]; then
                    docker rm -f wog_test_container
                fi
                """
                sh 'docker system prune -f'
                sh 'docker rmi ${DOCKER_IMAGE}'
                cleanWs()
            }
        }
    }
}
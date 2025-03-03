pipeline {
    agent any
    tools {
        'org.jenkinsci.plugins.docker.commons.tools.DockerTool' '27.3.1'
    }
    environment {
        REGISTRY = "borisgt/wog"
        FLASK_PORT = '8777'
        DOCKER_IMAGE = "${REGISTRY}:${BUILD_NUMBER}"
        PATH = "/usr/local/bin:$PATH"
        DOCKER_CERT_PATH = credentials('dockerhub_id')
        CONTAINER_FLASK = "wog_flask_container"
        CONTAINER_TEST = "wog_test_container"
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

        stage('Deploy image to Docker Hub') {
            steps {
                script {
                    sh """
                    docker push ${DOCKER_IMAGE}
                    """
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
                if [ \$(docker ps -aq -f name=${CONTAINER_FLASK}) ]; then
                    docker rm -f ${CONTAINER_FLASK}
                fi
                if [ \$(docker ps -aq -f name=${CONTAINER_TEST}) ]; then
                    docker rm -f ${CONTAINER_TEST}
                fi
                """
                sh 'docker system prune -f'
                sh 'docker rmi ${DOCKER_IMAGE}'
                cleanWs()
            }
        }
    }
}
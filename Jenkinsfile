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
        APP_URL = "http://localhost:${FLASK_PORT}"
        FLASK_SERVICE = "flask_wog"
    }

    triggers {
        pollSCM('H/5 * * * *') // Polls the SCM every 5 minutes
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
                    sh '''
                        echo $((RANDOM % 2001)) > Scores.txt
                    '''

                    sh 'chmod a+r Scores.txt'
                    sh 'docker compose build'
                }
            }
        }

        stage('Run') {
            when {
                expression { currentBuild.result != 'SUCCESS' }
            }
            steps {
                script {
                    sh 'docker compose up -d ${FLASK_SERVICE}'
                }
            }
        }

        stage('Test') {
            when {
                expression { currentBuild.result != 'SUCCESS' }
            }
            steps {
                script {
                    def testResult = sh(script: "docker exec ${CONTAINER_FLASK} sh -c 'sleep 10 && python3 /wog/tests/e2e.py ${APP_URL}'",
                        returnStatus: true)
                    if (testResult == 0) {
                        echo "Tests succeeded!"
                    } else {
                        error("Tests failed.")
                    }
                }
            }
        }

        stage('Deploy image to Docker Hub') {
            when {
                expression { currentBuild.result != 'SUCCESS' }
            }
            steps {
                script {
                    sh """
                    docker push ${DOCKER_IMAGE}
                    """
                }
            }
        }

        stage('Finalize') {
            when {
                expression { currentBuild.result != 'SUCCESS' }
            }
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
                    docker rm -vf ${CONTAINER_FLASK}
                fi
                """
                sh 'docker system prune -f'
                sh 'docker rmi ${DOCKER_IMAGE}'
                cleanWs()
            }
        }
    }
}
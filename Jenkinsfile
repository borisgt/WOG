pipeline {
    agent any
    tools {
        // a bit ugly because there is no `@Symbol` annotation for the DockerTool
        // see the discussion about this in PR 77 and PR 52:
        // https://github.com/jenkinsci/docker-commons-plugin/pull/77#discussion_r280910822
        // https://github.com/jenkinsci/docker-commons-plugin/pull/52
        'org.jenkinsci.plugins.docker.commons.tools.DockerTool' '27.3.1'
    }
    environment {
        REGISTRY = "borisgt/wog"
        REGISTRY_CREDENTIAL = 'dockerhub_id'
        FLASK_PORT = '8777'
        DOCKER_IMAGE = "${REGISTRY}:${BUILD_NUMBER}"
        PATH = "/usr/local/bin:$PATH"
        DOCKER_CERT_PATH = credentials('dockerhub_id')
    }

    stages {
        stage('Build') {
            steps {
                script {
                    echo "DOCKER_IMAGE is: ${DOCKER_IMAGE}"
                    sh 'docker info'
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
                    sh """
                    docker push ${DOCKER_IMAGE}
                    """
                    /*
                    docker.withRegistry( '', REGISTRY_CREDENTIAL ) {
                        DOCKER_IMAGE.push()
                    }
                    */
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
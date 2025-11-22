pipeline {
    agent any

    environment {
        SONARQUBE_SERVER = 'MySonar'
        DOCKER_IMAGE = 'dummy-login-python:latest'
        DOCKER_CONTAINER = 'dummy-login-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    def qg = waitForQualityGate()
                    if (qg.status != 'OK') {
                        error "❌ SECURITY FAILED: Issues found! Deployment blocked!"
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Deploy Container') {
            steps {
                sh """
                    if [ \$(docker ps -aq -f name=${DOCKER_CONTAINER}) ]; then
                        docker rm -f ${DOCKER_CONTAINER}
                    fi
                    docker run -d --name ${DOCKER_CONTAINER} ${DOCKER_IMAGE}
                """
            }
        }
    }

    post {
        always {
            echo "🎯 Pipeline Completed!"
        }
    }
}

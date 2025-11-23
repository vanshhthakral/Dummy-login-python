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
                    bat 'sonar-scanner.bat'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    timeout(time: 2, unit: 'MINUTES') {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "❌ SECURITY FAILED: Issues found! Deployment blocked!"
                        }
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                bat "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Deploy Container') {
            steps {
                bat """
                    docker stop ${DOCKER_CONTAINER} || true
                    docker rm ${DOCKER_CONTAINER} || true
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

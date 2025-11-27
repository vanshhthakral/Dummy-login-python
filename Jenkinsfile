pipeline {
    agent any

    environment {
        SONAR_HOST_URL = 'http://localhost:9000'
        SONAR_SCANNER = 'MySonarQube'
        SONAR_PROJECT_KEY = 'dummy-login'
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Pulling latest code..."
                git branch: 'main',
                    url: 'https://github.com/<your-username>/<your-repo>.git'
            }
        }

        stage("SonarQube Analysis") {
            steps {
                withSonarQubeEnv("${SONAR_SCANNER}") {
                    sh """
                        sonar-scanner \
                        -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                        -Dsonar.sources=. \
                        -Dsonar.python.version=3.10 \
                        -Dsonar.host.url=${SONAR_HOST_URL} \
                        -Dsonar.login=${SONAR_TOKEN}
                    """
                }
            }
        }

        stage("Docker Build") {
            steps {
                echo "Building Docker image..."
                sh "docker build -t dummy-login-app ."
            }
        }

        stage("Docker Run") {
            steps {
                echo 'Running application container...'
                sh "docker run --rm dummy-login-app"
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully ✔"
        }
        failure {
            echo "Pipeline failed ❌"
        }
    }
}

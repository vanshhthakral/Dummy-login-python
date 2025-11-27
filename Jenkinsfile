pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonar-token') // your SonarQube token
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling latest code...'
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube analysis...'
                withSonarQubeEnv('MySonarQube') {
                    // Using 'bat' for Windows
                    bat """
                    sonar-scanner ^
                    -Dsonar.projectKey=dummy-login ^
                    -Dsonar.sources=. ^
                    -Dsonar.host.url=http://localhost:9000 ^
                    -Dsonar.login=%SONAR_TOKEN%
                    """
                }
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t dummy-login .'
            }
        }

        stage('Docker Run') {
            steps {
                echo 'Running Docker container...'
                bat 'docker run --rm dummy-login'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! ✅'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
    }
}
